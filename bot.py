from config import keys
from selenium import webdriver

def order(key):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(key['product_url'])


# if __name__ == '__main':
order(keys)