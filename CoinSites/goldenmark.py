from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re


## url = https://goldenmark.com/pl/982-srebro-lokacyjne/s-2/waga-1_uncja?order=product.price.asc

def extract_price_from_information(information, price):
    value = re.findall('[0-9]+',information)
    priceReal = re.findall(r'\b\d+\b',price.replace(' ',''))
    return float(int(priceReal[0])/int(value[0]))

def goldenmark_main():
    url = "https://goldenmark.com/pl/982-srebro-lokacyjne/s-2/waga-1_uncja?order=product.price.asc"

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 2)
    coinsGridSelector = 'div.product > article:not(article.sold-out) > div > div.product-description'
    coinItems = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h2>a"))).text
        price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div.product-price-and-shipping >span"))).text
        sellPrice = price.replace('zł','').replace(',', ".")
        if 'Zestaw:' in name:
            try:
                sellPrice = extract_price_from_information(name, price)
            except Exception as e:
                print(e, f'during:{name}')

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


def goldon_main():
    return None