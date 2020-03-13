import json

data_path = '../data/final_data/dataset.json'

with open(data_path) as f:
    data = json.load(f)

all_news = []

for point in data:
    all_news += point['news']


titles = ['{}\t{}\n'.format(news['id'], news['title']) for news in all_news]
texts = ['{}\t{}\n'.format(news['id'], news['text'].replace('\n', '')) for news in all_news]

with open('../data/news_data/titles.txt', 'w') as f:
    f.writelines(titles)

with open('../data/news_data/texts.txt', 'w') as f:
    f.writelines(texts)