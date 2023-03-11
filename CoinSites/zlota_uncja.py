### to fix getting price ####


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def szlota_uncja_main():
    url = 'https://zlota-uncja.pl/pl/19-srebrne-monety-bulionowe?orderby=price&orderway=asc&id_category=19&n=48'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'ul.product_list > li >div >div>div:nth-child(1)>div'
    coinItems = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h5>a"))).text
        try:
            # print(price.get_attribute('innerText'))
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div span"))).text.replace('zł','').replace(',', ".")
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
    dane = szlota_uncja_main()
    print(dane)


