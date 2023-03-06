from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import re


## url = https://goldenmark.com/pl/982-srebro-lokacyjne/s-2/waga-1_uncja?order=product.price.asc

def extract_price_from_information(information, price):
    value = re.findall(r'\b\d+\b',information)
    priceReal = re.findall(r'\b\d+\b',price.replace(' ',''))
    return float(int(priceReal[0])/int(value[0]))
def goldenmark_main():
    url = "https://goldenmark.com/pl/982-srebro-lokacyjne/s-2/waga-1_uncja?order=product.price.asc"

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(2)
    coinsGridSelector = 'div.product > article:not(article.sold-out) > div > div.product-description'
    coinItems = driver.find_elements(by=By.CSS_SELECTOR, value=coinsGridSelector)

    driver.implicitly_wait(2)
    results = []
    for item in coinItems:
        driver.implicitly_wait(1)
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = item.find_element(by=By.CSS_SELECTOR, value=' h2 >a').text
        price = item.find_element(by=By.CSS_SELECTOR, value='div.product-price-and-shipping >span').text
        sellPrice = price
        if 'Zestaw:' in name:
            sellPrice = extract_price_from_information(name, price)


        buyPriceItems = None

        driver.implicitly_wait(2)
        result = {'Sprzedaż':sellPrice,
                   'Kupno':buyPriceItems,
                  'Nazwa':name
                   }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = goldenmark_main()
    print(dane)