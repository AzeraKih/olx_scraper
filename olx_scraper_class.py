from selenium import webdriver
from item_class import item_class as item
from selenium.webdriver.chrome.options import Options

class olx_scraper_class:
    
    driver = None
    options = Options()

    def __init__(self):
        self.options.add_argument("--log-level=3")
        #Altere para a pasta onde o chromedriver for instalado.
        self.driver = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver.exe", chrome_options=self.options)
        return
    
    def close(self):
        self.driver.quit()

    def get_elements(self, url):
        self.driver.get(url)
        content = self.driver.find_elements_by_class_name("fnmrjs-1")

        products = []

        for a in content:
            name=a.find_elements_by_class_name('fnmrjs-6')
            lbl_price=a.find_elements_by_class_name('fnmrjs-7')
            location=a.find_elements_by_class_name('fnmrjs-5')
            
            price = lbl_price[0].find_element_by_css_selector('span.eoKYee').text
            lbl_price = lbl_price[0].find_elements_by_css_selector('.wlwg1t-1.fsgKJO.sc-ifAKCX.eLPYJb')
            data = lbl_price[0].text
            hora = lbl_price[1].text

            location = location[0].find_element_by_css_selector('span.ciykCV').text
            name = name[0].find_element_by_css_selector('h2.eJfLou').text
            
            if data == 'Hoje' or data == 'Ontem':
                product = item(name, price, location, data, hora)
                products.append(product)

        return products