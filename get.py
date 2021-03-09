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

