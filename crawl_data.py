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

def crawl_page(url, data_type):
    driver.get(url)

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
            header = driver.find_element_by_css_selector('.article-hero-title>h1.heading')
            link_data[index]['title'] = header.text
        except Exception as e:
            continue
        try:
            body = driver.find_element_by_css_selector('.article-body')
            paragraphs = body.find_elements_by_css_selector('.article-pharagraph')[1:]
            text = ''

            for paragraph in paragraphs:
                text += paragraph.text + '\n'
            
            if len(text) == 0:
                paragraphs = driver.find_elements_by_css_selector('.classic-body p')
                for paragraph in paragraphs:
                    text += paragraph.text + '\n'
            link_data[index]['text'] = text
        except Exception as e:
            continue

    driver.quit()
    final_data = []
    for link in link_data:
        if 'text' in link.keys():
            if len(link['text']) > 0:
                final_data.append(link)
    with open('./data/coindesk_data/bitcoin_article_data_{}.json'.format(data_type), 'w') as f:
        json.dump(final_data, f, indent=4)

if __name__ == "__main__":
    urls = [
        ['https://www.coindesk.com/news', 'news'],
        ['https://www.coindesk.com/opinion', 'opinion'],
        ['https://www.coindesk.com/features', 'features'],
        ['https://www.coindesk.com/category/markets', 'markets'],
        ['https://www.coindesk.com/category/tech', 'tech'],
        ['https://www.coindesk.com/category/business', 'business'],
        ['https://www.coindesk.com/category/policy-regulation', 'policy-regulation'],
        ['https://www.coindesk.com/category/people', 'people'],
        ['https://www.coindesk.com/tag/price-news', 'price']
        ]
    for url in urls:
        driver = create_driver()
        print('='*25)
        print('Crawling Topic: {}'.format(url[1]))
        crawl_page(url[0], url[1])
        time.sleep(250)
        driver.quit()

        print('\n'*5)