import requests

url = 'https://bit.ly/3ccGLhN'
r = requests.get(url, stream=True).raw
