from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def metalmarket_main():
    url = 'https://www.metalmarket.eu/pl/menu/srebrne-monety-851.html?filter_traits%5B1%5D=367&filter_traits%5B510%5D=481'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get(url)
    dropDownSelector = "div#paging_setting_top form.--sort > div.f-dropdown.s_paging__select:nth-child(1)"

    submit_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, dropDownSelector)))
    submit_button.click()

    optionsSelector = 'div#paging_setting_top form.--sort div.f-dropdown.s_paging__select > ul.f-dropdown-menu >li.f-dropdown-li>a'
    options = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, optionsSelector)))
    for option in options:
        print(option.get_attribute("innerText"))
        if 'cenie rosnąco' in option.get_attribute("innerText"):
            try:
                option.click()
            except Exception as e:
                print(e)
            break

    coinsGridSelector = 'section.products > div'
    coinItems = wait.until(
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
    dane = metalmarket_main()
    print(dane)


