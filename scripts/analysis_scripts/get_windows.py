import json


def get_windows(data, window_size=5):
    windows = []
    # start from index window size (with windows of default of 5)
    for i in range(window_size, len(data)):
        window = {
            'data': data[i - window_size:i],
            'label': data[i]['label']
        }

        windows.append(window)
    return windows


if __name__ == "__main__":
    with open('../../data/experimental_data/sentiment_and_labels.json') as f:
        data = json.load(f)
    windows = get_windows(data)
    with open('../../data/experimental_data/windows.json', 'w') as f:
        json.dump(windows, f, indent=4)
    print('Created {} windows'.format(len(windows)))
