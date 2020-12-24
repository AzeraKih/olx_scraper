# olx_scraper
um scraper feito para alertar sobre novos anuncios postados.

Este codigo foi desenvolvido em python 3.9 para alertar via email novos anuncios publicados na OLX baseado nas pesquisas cadastradas.

Para utilização, é necessario a instalação dos pacotes abaixo:

pip install beautifulsoup4
pip install selenium

É preciso fazer o download do chromedriver, para realizar o webscrapping:
https://chromedriver.chromium.org/downloads
Por padrão, salve-o na pasta: C:\Chrome\chromedriver.exe

Na primeira execução do codigo, rode o arquivo "init_load", ele fará o scrapping de todos os anuncios e não fará o alerta inicial, após isso rode o arquivo run.ps1
Você pode agendar uma task para rodar a cada 15 minutos este arquivo .ps1, ele irá logar tudo dentro da pasta log.
Não esqueça de configurar seus Emails na função "sendEmail" do arquivo main.py