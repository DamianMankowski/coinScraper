from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## url = https://tavex.pl/srebro/srebrne-monety-bulionowe/page/1/?meta%5B0%5D=tax-silver%3Asrebrne-monety-bulionowe&sorting=price_asc



def tavex_main():
    url = "https://tavex.pl/srebro/srebrne-monety-bulionowe/page/1/?meta%5B0%5D=tax-silver%3Asrebrne-monety-bulionowe&sorting=price_asc"

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(2)

    addButtonSelector = 'form > div:nth-child(1) > a'
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=addButtonSelector)
    submit_button.click()

    wait = WebDriverWait(driver, 2)

    coinsGridSelector = 'div.v-category__content > div.grid--narrow-xs > div > a'
    coinItems = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, coinsGridSelector)))

    results = []
    for i, item in enumerate(coinItems):
        information = wait.until(EC.visibility_of(item.find_element(by=By.CSS_SELECTOR, value="div.product__meta")))
        name = information.find_element(by=By.CSS_SELECTOR, value = 'div > h3 > span').text
        try:
            prices = item.find_elements(by=By.CSS_SELECTOR, value='div.product__prices > div')
            sellPrice = prices[0].find_element(by=By.CSS_SELECTOR, value='span.product__price-value').text.replace('zł',
                                                                                                                   '').replace(
                ',', ".")
            buyPriceItems = prices[2].find_elements(by=By.CSS_SELECTOR,
                                                    value='div.product__prices > div.product__price--buy >span:nth-child(2) >span>span>span') if len(
                prices) == 3 else prices[1].find_elements(by=By.CSS_SELECTOR,
                                                          value='div.product__prices > div.product__price--buy >span:nth-child(2) >span>span>span')

        except Exception as e:
            print(e, f'during:{name}')
            continue


        tmp = []
        for buyItem in buyPriceItems:
            tmp.append(buyItem.text)
        buyPrice = ''.join(tmp).replace(',','.')
        driver.implicitly_wait(2)
        result = {'Sprzedaż':sellPrice,
                   'Kupno':buyPrice,
                  'Nazwa':name
                   }
        results.append(result)

    df = pd.DataFrame.from_records(results)
    return df


if __name__ == '__main__':
    dane = tavex_main()
    print(dane)