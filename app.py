import os.path

SRC = 'src.png'
DST = 'dst.png'

if not os.path.isfile(SRC):
    import requests

    url = 'https://bit.ly/3ccGLhN'
    r = requests.get(url, stream=True).raw

    from PIL import Image

    img = Image.open(r)
    img.save(SRC)
    print(img.get_format_mimetype)

if not os.path.isfile(DST):
    BUF_SIZE=1024
    with open(SRC, 'rb') as sf, open(DST, 'wb') as df:
        while True:
            data = sf.read(BUF_SIZE)
            if not data:
                break
            df.write(data)

import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open(SRC, 'rb') as sf, open(DST, 'rb') as df:
  sha_src.update(sf.read())
  sha_dst.update(df.read())

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dst_img = mpimg.imread(DST)
print(dst_img)
