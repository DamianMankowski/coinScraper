from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def element79_main():
    url = 'https://79element.pl/srebrne-monety-1-oz/?orderby=price'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'ul.products>li'
    coinItems = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h2"))).text
        try:
            # print(price.get_attribute('innerText'))
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="span>span>bdi"))).text.replace('zł','').replace(',', ".")
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
    dane = element79_main()
    print(dane)


