from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mennica_mazovia_main():
    url = 'https://mennicamazovia.pl/pol_m_Srebro_Srebrne-Monety-158.html?filter_pricerange=&filter_traits%5B41%5D=65&filter_traits%5B31%5D=&filter_traits%5B276%5D='

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'section.products>div'
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="h3>a"))).text
        try:
            price = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div>strong"))).text.replace('zł','').replace(',', ".")
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
    dane = mennica_mazovia_main()
    print(dane)


