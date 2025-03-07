#Fetch a webpage,check if the request was succesful and extract the main heading text from the page',s
# content you can assume that the base url is 'https://example.com'

import requests
from bs4 import BeautifulSoup

url  = 'https://example.com'

response = requests.get(url)

if response.status_code == 200:
    print('Success')
    print(response.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.h1
    if h1_tag:
        print(h1_tag.text)  
    else:
        print('No <h1> tag found')
else:
    print('Failed',response.status_code)
    