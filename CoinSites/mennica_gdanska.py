from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mennica_gdanska_main():
    url = 'https://mennica-gdanska.pl/pl/43-monety-srebrne?order=product.price.asc'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'div.products div.item-product article div.desc_info'
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h4>a"))).text
        try:
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div span.price"))).text.replace('zł','').replace(',', ".")
        except Exception as e:
            print(e, f'during:{name}')
            continue
        buyPrice = None
        result = {'Sprzedaż':price,
                   'Kupno':buyPrice,
                  'Nazwa':name
                   }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = mennica_gdanska_main()
    print(dane)


