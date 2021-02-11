import requests

headers = {
    'Ocp-Apim-Subscription-Key': '621deae3d9184b97b93c599e91824ae7',
}

params = (
    ('q', 'sedan'),
    ('customconfig', '5a9e651c-63f6-47e4-a603-db31b2b7fd82'),
)

response = requests.get('https://api.bing.microsoft.com/v7.0/custom/suggestions/search', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.bing.microsoft.com/v7.0/custom/suggestions/search?q=sedan&customconfig=5a9e651c-63f6-47e4-a603-db31b2b7fd82', headers=headers)
