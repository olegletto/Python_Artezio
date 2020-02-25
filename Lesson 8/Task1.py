import requests


def site_request(a):
    response = requests.get(a)
    return len(response.text)


print(site_request('https://google.com'))
