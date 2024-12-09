import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set up Kaggle API credentials (if not in ~/.kaggle/kaggle.json)
os.environ['KAGGLE_USERNAME'] = 'uname'
os.environ['KAGGLE_KEY'] = 'Kaggle_API'

# Initialize API
api = KaggleApi()
api.authenticate()

# Download and unzip dataset
dataset_name = 'mlg-ulb/creditcardfraud'
destination_path = './datasets'
api.dataset_download_files(dataset_name, path=destination_path, unzip=True)

print(f"Dataset downloaded and unzipped at: {destination_path}")
