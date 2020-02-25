import requests
import base64


def image_size(img_path: str, img_name: str):

    file = open(img_path, 'rb')
    response = requests.post('https://postman-echo.com/post', files=file)
    dlfile = response.json()['files']
    image = base64.b64decode(dlfile)
    img_name.write(image)
    return len(image)


print(image_size('assets/bild.jpg', 'assets/postfile.jpg'))