import os
import requests
import urllib.request
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get('API_KEY')
img_path = os.environ.get('IMAGE_PATH')
response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
data = response.json()
img_url = data.get('hdurl')
if img_url is None:
    exit()

urllib.request.urlretrieve(img_url, img_path)


