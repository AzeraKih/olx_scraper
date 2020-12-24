from item_class import item_class as item
from olx_scraper_class import olx_scraper_class as olx_scraper
from config import links

olx_scpr = olx_scraper()
newProducts = []

for link in links:
    [newProducts.append(a) for a in olx_scpr.get_elements(link['url'])]

item.save_data('data', newProducts)