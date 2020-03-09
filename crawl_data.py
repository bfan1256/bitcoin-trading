import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver_80', options=chrome_options)

start_url = "https://www.coindesk.com/opinion"
driver.get(start_url)

link_data = [] 
count = 0

def find_more():
    try:
        return driver.find_element_by_css_selector('div.cta-content > div.no-js-only > a').get_attribute('href')
    except Exception:
        return False

driver.get(find_more())



while find_more():
    
    driver.get(find_more())
    cards = driver.find_elements_by_css_selector('.list-item-card')
    
    for card in cards:
        data = {}
        links = card.find_elements_by_css_selector('.text-content a')
        article_link = ''
        for link in links:
            if link.get_attribute('title') != '': 
                data['link'] = link.get_attribute('href')
                break
        data['author'] = card.find_element_by_css_selector('.card-desc-block .credit').text
        data['date'] = card.find_element_by_css_selector('.card-desc-block .time').text
        link_data.append(data)
    count += 1
    if count % 10 == 0:
        print('Total Article Data: {} Articles'.format(len(link_data)))


for index, data in enumerate(tqdm(link_data)):
    driver.get(data['link'])
    try:
        body = driver.find_element_by_css_selector('.article-body')
        paragraphs = body.find_elements_by_css_selector('.article-pharagraph')[1:]
        text = ''
        for paragraph in paragraphs:
            text += paragraph.text + '\n'
        link_data[index]['text'] = text
    except Exception:
        continue

driver.quit()

with open('bitcoin_article_data.json', 'w') as f:
    json.dump(link_data, f, indent=4)