from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def guldener_main():
    url = 'https://guldener.pl/kategoria-29-1-uncja-srebra-monety-inwestycyjne?order=product.price.asc'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    coinsGridSelector = 'div.products article'
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        information = wait.until(EC.visibility_of(item.find_element(by=By.CLASS_NAME, value="product-price-and-shipping"))).find_element(by=By.CSS_SELECTOR, value='div')
        name = information.get_attribute('data-product-name')
        try:
            price = information.get_attribute("data-product-price").replace('zł','').replace(',', ".")
        except Exception as e:
            print(e, f'during:{name}')
            continue
        buyPrice = None
        result = {'Sprzedaż':price,
                   'Kupno':buyPrice,
                  'Nazwa':name,
                  'Strona':url,
                   }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = guldener_main()
    print(dane)


