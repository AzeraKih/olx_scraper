from item_class import item_class as item
from olx_scraper_class import olx_scraper_class as olx_scraper
from config import links
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import smtplib

def sendEmail(msg):

    emailFrom = 'seu_email@gmail.com'
    emailTo = ['email_destino@outlook.com']
    emailSubject = 'Novos anuncions encontrados'

    mimeMsg = MIMEMultipart()
    mimeMsg["From"] = emailFrom
    mimeMsg["To"] = ','.join(emailTo)
    mimeMsg["Subject"] = emailSubject
    mimeMsg.attach(MIMEText(msg,'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #usando o gmail.
        server.ehlo()
        server.login(emailFrom, 'sua_senha')
        server.send_message(mimeMsg)
        server.close()

        print('Email enviado!')

    except Exception as e:
        print('Algo deu errado...')
        print(e)

    return None

def Diff(newProducts, oldProducts):
    newIDs = [n.name + ' - ' + n.hour for n in newProducts]
    oldIDs = [n.name + ' - ' + n.hour for n in oldProducts]
    alertNewPdts = []
    for newID in newIDs:
        if newID not in oldIDs:
            alertNewPdts.append(item.find(newProducts, newID))

    return alertNewPdts

olx_scpr = olx_scraper()
newProducts = []

for link in links:
    print('%s Coletando informacoes de: %s ...' %( 
    str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")), link['name']))

    [newProducts.append(a) for a in olx_scpr.get_elements(link['url'])]

oldProducts = item.read_data('data')
item.save_data('data', newProducts)
lDiff = Diff(newProducts, oldProducts)


if len(lDiff) < 1:
    print('Nenhum anuncio novo :/')
else:
    headerEmail = ('#'*60) + '\n FORAM ENCONTRADOS NOVOS ITENS A VENDA! \n' + ('#'*60) + '\n'
    strEmail = ''
    for a in lDiff:
        strEmail += (str(a) + '\n' + ('#'*60) + '\n')

    print('\nNovos Itens: \n%s'%strEmail)
    sendEmail(headerEmail + strEmail)

olx_scpr.close()