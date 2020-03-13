import json
import argparse
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculate_sentiments(file):
    f = open(file)
    data = json.load(f)
    f.close()
    sid = SentimentIntensityAnalyzer()
    for data_index, point in enumerate(data):
        for index, article in enumerate(point['news']):
            if 'text' in article.keys():
                sentiment = TextBlob(article['text']).sentiment
                article['text-polarity'] = sentiment.polarity
                article['text-subjectivity'] = sentiment.subjectivity
            
            article['title-polarity'] = sid.polarity_scores(article['title'])['compound']
            point['news'][index] = article
        data[data_index] = point
    return data

def calculate_sentiments_by_dict(data):
    sid = SentimentIntensityAnalyzer()
    for data_index, point in enumerate(data):
        for index, article in enumerate(point['news']):
            if 'text' in article.keys():
                sentiment = TextBlob(article['text']).sentiment
                article['text-polarity'] = sentiment.polarity
                article['text-subjectivity'] = sentiment.subjectivity
            article['title-polarity'] = sid.polarity_scores(article['title'])['compound']
            point['news'][index] = article
        data[data_index] = point
    return data

def calculate_sentiment(text):
    return TextBlob(text).sentiment

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('destination')

    args = parser.parse_args()

    with open(args.destination, 'w') as f:
        json.dump(calculate_sentiments(args.path), f, indent=4)