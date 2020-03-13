import json
from get_turnpoints import getBottoms, getTops
from sentiment import calculate_sentiments_by_dict

with open('../../data/final_data/only_title_data/dataset_augmented_0.4_only_titles.json') as f:
    data = json.load(f)

prices = [point['close'] for point in data]

bottoms = getBottoms(prices)
tops = getTops(prices)

final_data = calculate_sentiments_by_dict(data)

indices_not_zero = []

for bottom in bottoms:
    final_data[bottom[0]]['label'] = {}
    final_data[bottom[0]]['label']['numerical'] = 1
    final_data[bottom[0]]['label']['categorical'] = 'buy'
    indices_not_zero.append(bottom[0])
for top in tops:
    final_data[top[0]]['label'] = {}
    final_data[top[0]]['label']['numerical'] = 2
    final_data[top[0]]['label']['categorical'] = 'sell'
    indices_not_zero.append(top[0])

for index in range(len(final_data)):
    if index not in indices_not_zero:
        final_data[index]['label'] = {}
        final_data[index]['label']['numerical'] = 0
        final_data[index]['label']['categorical'] = 'hold'

with open('../../data/experimental_data/sentiment_and_labels.json', 'w') as f:
    json.dump(final_data, f, indent=4)

print('I found {} bottoms and {} tops'.format(len(bottoms), len(tops)))