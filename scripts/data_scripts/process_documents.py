import json
import uuid
from glob import glob

data_path = '../data/coindesk_data/*.json'

data_files = glob(data_path)

article_links = []
articles = []
filtered_articles = []
for file in data_files:
    with open(file) as f:
        articles += json.load(f)

print('Found a Total of {} Articles (Unfiltered)'.format(len(articles)))

for article in articles:
    if article['link'] not in article_links:
        article_links.append(article['link'])
        article['id'] = str(uuid.uuid4())
        filtered_articles.append(article)


print('Total # of Filtered Articles: {} Articles'.format(len(filtered_articles)))

with open('../data/final_data/all_news.json', 'w') as f:
    json.dump(filtered_articles, f, indent=4)