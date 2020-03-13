import json

data_path = '../data/bitcoin_data/prices.json'

with open(data_path) as f:
    data = json.load(f)

new_data = []
for currency in data:
    currency_data = []
    for index, timestamp in enumerate(currency['timestamps']):
        price_timestamp = {
            'price': currency['prices'][index],
            'timestamp': currency['timestamps'][index]
        }
        currency_data.append(price_timestamp)
    currency_obj = {
        'currency': currency['currency'],
        'prices': currency_data
    }
    new_data.append(currency_obj)


with open('../data/final_data/prices.json', 'w') as f:
    json.dump(new_data, f, indent=4)