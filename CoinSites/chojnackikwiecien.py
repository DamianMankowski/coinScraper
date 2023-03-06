from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilis.helper import extract_price_from_information
import pandas as pd

## url = https://chojnackikwiecien.pl/sklep/?orderby=price&filter_metal=srebro&query_type_metal=or&filter_forma=monety&query_type_forma=or

def chojnackikwiecien_main():
    url = "https://chojnackikwiecien.pl/sklep/?orderby=price&filter_metal=srebro&query_type_metal=or&filter_forma=monety&query_type_forma=or"

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(2)
    coinsGridSelector = '#primary > div > div.inner-wrap > article > ul >li >div>div>div:nth-child(2)'
    coinItems = driver.find_elements(by=By.CSS_SELECTOR, value=coinsGridSelector)

    driver.implicitly_wait(2)
    results = []
    for i, item in enumerate(coinItems):
        name = item.find_element(by=By.CSS_SELECTOR, value=' h4>a').text
        price = item.find_element(by=By.CSS_SELECTOR, value='span>span').text
        properPrice = extract_price_from_information(name, price)


        sellPrice = properPrice
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
    dane = chojnackikwiecien_main()
    print(dane)