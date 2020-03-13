import json

price_data_path = '../data/final_data/prices_with_ma.json'
news_data_path = '../data/final_data/all_news.json'

with open(price_data_path) as f:
    price_data = json.load(f)

with open(news_data_path) as f:
    news_data = json.load(f)

final_data = []
for price in price_data:
    if price['SMA_200'] == 0:
        continue
    news_for_price = []
    for news in news_data:
        if price['date'] == news['date']:
            news_for_price.append(news)
    price['news'] = news_for_price
    final_data.append(price)

with open('../data/final_data/dataset.json', 'w') as f:
    news_data = json.dump(final_data, f, indent=4)