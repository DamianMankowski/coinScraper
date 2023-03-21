import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_price_from_information(information, price):
    value = re.findall(r'\b\d+\b',information)
    priceReal = re.findall(r'\b\d+\b',price.replace(' ','').replace('zł',''))
    return float(int(priceReal[0])/int(value[0]))
def mennicakapitalowa_main():
    url = 'https://mennicakapitalowa.pl/pol_m_Srebro_MONETY-BULIONOWE-175.html'

    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 5)

    driver.get(url)

    coinsGridSelector = 'div.table_row >div'
    coinItems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        name = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="a:nth-child(3)"))).text
        try:
            prices = item.find_element(by=By.CSS_SELECTOR, value='div.product_prices>span').text
        except Exception as e:
            print(e, f'during:{name}')
            continue

        properPrice = extract_price_from_information(name,prices)

        buyPrice = None
        result = {'Sprzedaż':properPrice,
                   'Kupno':buyPrice,
                  'Nazwa':name,
                  'Strona':url,
                   }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = mennicakapitalowa_main()
    print(dane)


