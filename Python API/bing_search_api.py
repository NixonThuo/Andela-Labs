
import requests


def bing_search(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    # query string parameters
    payload = {'q': query}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': 'aef765d25f7c46298ce2fe5d8b4773a5'}
    # make GET request
    data = requests.get(url, params=payload, headers=headers)
    # get JSON response
    data = data.json()
    return data


print bing_search('Andela')
