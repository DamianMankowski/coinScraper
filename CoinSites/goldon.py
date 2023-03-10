from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def goldon_main():
    url = 'https://www.goldon.pl/srebrne-monety-bulionowe-a/masa-1-oz,dCw-FA.html?sort=price_asc'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 2)

    coinsGridSelector = 'div.products_container article'
    coinItems = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div a >img"))).get_attribute("alt")
        try:
            price = item.find_element(by=By.CSS_SELECTOR, value='footer >div:nth-child(2)>div>span').get_attribute("content")
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
    dane = goldon_main()
    print(dane)


