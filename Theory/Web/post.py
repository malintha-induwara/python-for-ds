import requests

data = {'user_name': 'admin', 'password': 'admin'}

url = 'https://httpbin.org/post'

response = requests.post(url, data)

if response.status_code == 200:
    print('Login succes')
    print(response.text)
else:
    print('Login Failed',response.status_code)
