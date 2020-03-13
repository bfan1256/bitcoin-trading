python prep_augmentation.py
python ./augment.py --input=../data/news_data/titles.txt --output=../data/augmented_news_data/titles_augmented_0.4.txt --num_aug=16 --alpha=0.4
python ./augment.py --input=../data/news_data/titles.txt --output=../data/augmented_news_data/titles_augmented_0.3.txt --num_aug=16 --alpha=0.3
python ./augment.py --input=../data/news_data/titles.txt --output=../data/augmented_news_data/titles_augmented_0.2.txt --num_aug=16 --alpha=0.2
python ./augment.py --input=../data/news_data/titles.txt --output=../data/augmented_news_data/titles_augmented_0.1.txt --num_aug=16 --alpha=0.1
python ./augment.py --input=../data/news_data/titles.txt --output=../data/augmented_news_data/titles_augmented_0.05.txt --num_aug=16 --alpha=0.05
python ./create_augmented_dataset.py