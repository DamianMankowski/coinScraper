from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def numizmatyczny_main():
    url = 'https://numizmatyczny.com/monety-srebrne-1-uncja/1/default/3'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'div.products >div >div'
    coinItems = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div.product-short-description>p"))).text
        try:
            # print(price.get_attribute('innerText'))
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div.row >div> em"))).text.replace('zł','').replace(',', ".").replace('od ','')
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
    dane = numizmatyczny_main()
    print(dane)


