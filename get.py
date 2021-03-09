import requests

url = 'https://bit.ly/3ccGLhN'
r = requests.get(url, stream=True).raw

from PIL import Image

img = Image.open(r)
img.save('src.png')
print(img.get_format_mimetype)
