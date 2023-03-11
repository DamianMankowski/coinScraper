from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mennicaskarbowa_main():
    url = 'https://www.mennicaskarbowa.pl/pol_m_Srebro_Srebrne-monety-151.html'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'div.row > div.product_wrapper>div'
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="a:nth-child(2)"))).text
        try:
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div>span"))).text.replace('zł','').replace(',', ".")
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
    dane = mennicaskarbowa_main()
    print(dane)


