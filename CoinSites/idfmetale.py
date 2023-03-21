from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def idfmetale_main():
    url = 'https://idfmetale.pl/srebrne-monety-bulionowe/1/default/3'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = "div.products >div>div.product-inner-wrap"
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        try:
            skip = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div.buttons >form.availability-notifier")))
        except Exception as e:
            print(e)
            continue
        # time.sleep(5)
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="a:nth-child(2)>span"))).text

        script = f"return window.getComputedStyle(document.querySelectorAll('.price>em'){[i]}," \
                 "'::before').getPropertyValue('content')";

        element = driver.execute_script(script);
        print(element)

        try:
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value=".price>em"))).text.replace('zł','').replace(',', ".")
        except Exception as e:
            print(e, f'during:{name}')
            continue
        print(price,name)
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
    dane = idfmetale_main()
    print(dane)


