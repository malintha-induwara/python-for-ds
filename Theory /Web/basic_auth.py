import requests


url = "https://httpbin.org/get"

user_name = 'admin'
password = 'admin'


response = requests.get(url, auth=(user_name, password))

if response.status_code == 200:
    print('Success')
    print(response.url)
    print(response.text)