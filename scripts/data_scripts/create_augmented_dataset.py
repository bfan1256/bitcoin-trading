import json
from tqdm import tqdm
from glob import glob

dataset_path = '../data/final_data/dataset.json'
augmented_data_path = '../data/augmented_news_data/'
file_paths = glob(augmented_data_path + '*.txt')

with open(dataset_path) as f:
    data = json.load(f)

articles = {}
for index, point in enumerate(data):
    for article in point['news']:
        article['data-point'] = index
        articles[article['id']] = article

for file in tqdm(file_paths):
    f = open(file)
    augmented_amount = file.split('_')[-1].split('.txt')[0]
    titles = f.readlines()
    for title in titles:
        title_data = title.split('\t')
        article_id = title_data[0]
        article = articles[article_id]
        if type(article['title']) != list:
            article['title'] = [article['title']]
        article['title'] = title_data[1]
        point_index = article['data-point']
        new_article =  {i:article[i] for i in article if (i!='data-point' and i!='text')}
        data[point_index]['news'].append(new_article)

        
    with open('../data/final_data/dataset_augmented_{}_titles_only.json'.format(augmented_amount), 'w') as f:
        json.dump(data, f, indent=4)
    f.close()