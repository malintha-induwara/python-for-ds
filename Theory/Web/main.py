import requests


response = requests.get('https://api.github.com/events')


if response.status_code == 200:
    # print(response.headers)

    # Extract response details
    print(response.headers['Content-Type'])


    # Extract response details
    # print(response.text)


    #Extract response as JSON
    print(response.json()[3])

    
    # Extract response details
    print("Successflly fetched the page")
else:
    print("Some error happedn while fetching the data")