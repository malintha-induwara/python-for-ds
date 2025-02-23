import requests

url  = 'https://example.com'

params = {'q':'python','category':'books'}


response = requests.get(url, params=params)


if response.status_code == 200:
    print('Success')
    print(response.url)
else:
    print('Failed',response.status_code)