import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    return driver

def crawl_page():
    driver = create_driver()
    driver.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20200310')
    
    rows = driver.find_elements_by_css_selector('tr.cmc-table-row')
    print('Found {} rows'.format(len(rows)))
    data = []
    for row in tqdm(rows):
        price_data = {}
        values = row.find_elements_by_css_selector('td>div')
        price_data['date'] = values[0].text
        price_data['open'] = float(values[1].text.replace(',', ''))
        price_data['close'] = float(values[4].text.replace(',', ''))
        price_data['volume'] = int(values[5].text.replace(',', ''))
        price_data['market-cap'] = int(values[-1].text.replace(',', ''))
        data.append(price_data)

    driver.quit()

    with open('./data/bitcoin_data/bitcoin_price_data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    crawl_page()