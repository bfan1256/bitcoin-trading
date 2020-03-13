import json
import pandas as pd

with open('./data/bitcoin_data/bitcoin_price_data.json') as f:
    data = json.load(f)


def process_currency(currency):
    df = pd.DataFrame(reversed(currency))
    df['SMA_20'] = df.close.rolling(window=20).mean().fillna(0)
    df['SMA_50'] = df.close.rolling(window=50).mean().fillna(0)
    df['SMA_100'] = df.close.rolling(window=100).mean().fillna(0)
    df['SMA_150'] = df.close.rolling(window=150).mean().fillna(0)
    df['SMA_200'] = df.close.rolling(window=200).mean().fillna(0)
    df['EMA_20'] = df.close.ewm(span=20, adjust=False).mean().fillna(0)
    df['EMA_50'] = df.close.ewm(span=50, adjust=False).mean().fillna(0)
    df['EMA_100'] = df.close.ewm(span=100, adjust=False).mean().fillna(0)
    df['EMA_150'] = df.close.ewm(span=150, adjust=False).mean().fillna(0)
    df['EMA_200'] = df.close.ewm(span=200, adjust=False).mean().fillna(0)
    return df.to_dict('records')

new_currency_data = process_currency(data)

with open('./data/final_data/prices_with_ma.json', 'w') as f:
    json.dump(new_currency_data, f, indent=4)

