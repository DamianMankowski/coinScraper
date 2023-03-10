from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import re


## url = https://flyingatom.gold/23-srebrne-monety-bulionowe?order=product.price.asc



def flyingatom_main():
    url = "https://flyingatom.gold/23-srebrne-monety-bulionowe?order=product.price.asc"

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(2)

    # addButtonSelector = 'form > div:nth-child(1) > a'
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value=addButtonSelector)
    # submit_button.click()

    # driver.implicitly_wait(5)

    coinsGridSelector = '#js-product-list > div.products.product-thumbs.row > div > article >a >div>div:nth-child(2)>div:nth-child(2)'
    coinItems = driver.find_elements(by=By.CSS_SELECTOR, value=coinsGridSelector)

    results = []
    for i, item in enumerate(coinItems):
        name = item.find_element(by=By.CSS_SELECTOR, value='span').text
        sell = item.find_element(by=By.CSS_SELECTOR, value='div.product-price-and-shipping>span:nth-child(2)').text
        buy = item.find_element(by=By.CSS_SELECTOR, value='div:nth-child(5) > span').text

        # print(len(prices))

        sellPrice = re.findall(r'\b\d+\b',sell)
        buyPrice = re.findall(r'\b\d+\b',buy)
        driver.implicitly_wait(2)

        result = {'Sprzedaż':sellPrice[0],
                   'Kupno':buyPrice[0],
                  'Nazwa': name
                  }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = flyingatom_main()
    print(dane)