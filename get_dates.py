import json
from glob import glob
from datetime import datetime

path = './data/coindesk_data'

data_files = glob(path + '/*.json')

def process_date(string):
    return datetime.strptime(string, '%b %d, %Y').date()


earliest_date = None
latest_date = None
for file in data_files:
    with open(file) as f:
        data = json.load(f)
        for article in data:
            if earliest_date == None:
                earliest_date = process_date(article['date'])
                continue
            else:
                if earliest_date > process_date(article['date']):
                    earliest_date = process_date(article['date'])
            
            if latest_date == None:
                latest_date = process_date(article['date'])
                continue
            else:
                if latest_date < process_date(article['date']):
                    latest_date = process_date(article['date'])

print('Latest Date: {}'.format(latest_date))
print('Earliest Date: {}'.format(earliest_date))