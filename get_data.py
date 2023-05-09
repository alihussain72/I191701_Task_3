import os
import wget

# data from https://www.kaggle.com/datasets/himanshunakrani/iris-dataset

# Download the zipped dataset
url = 'https://www.kaggle.com/datasets/himanshunakrani/iris-dataset/rawdata_new.csv?sequence=1&isAllowed=y'
file_name = "data_raw.csv"
wget.download(url, file_name)
