from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def srebnamennica_main():
    url = 'https://srebrnamennica.pl/11-srebrne-monety-bulionowe?proba=0-999&waga=1-uncja&order=product.price.asc'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'div.products div.product-description'
    coinItems = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h3>a>span"))).text
        try:
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="span.price"))).text.replace('zł','').replace(',', ".")
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
    dane = srebnamennica_main()
    print(dane)


