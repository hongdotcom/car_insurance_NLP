
import requests
import urllib

def bing_search(searchTxt):

    headers = {
    'Ocp-Apim-Subscription-Key': '621deae3d9184b97b93c599e91824ae7',
}
    payload = (
    ('q', searchTxt),
    ('customconfig', '5a9e651c-63f6-47e4-a603-db31b2b7fd82'),
    ('mkt', 'en-US'),
    ('safesearch','Off'),
)
    params = urllib.parse.urlencode(payload)
    res  = requests.get('https://api.bing.microsoft.com/v7.0/custom/search', params=params, headers=headers)
    print('bing')
    result = res.json()
    displayTxt = {}
    for item in result["webPages"]["value"]:
      
      displayTxt[item["name"]] = item["url"]
    # print(displayTxt)
    return displayTxt

def nlp_check(searchTxt):
   
    headers = {
        'Content-Type': 'application/json',
    }
    params = (
        ('version', '2019-07-12'),
    )
    txt = "{}".format(searchTxt)
    target = '"car","insurance","coupe","sedan","suv","pickup truck"'
    data = '{ "text":"' + txt + '", "features": { "sentiment": { "targets": [' + target + '] }, "keywords": { "emotion": true } } }'
    res = requests.post('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/f64d5fec-a1be-424e-bdc0-df1c15e1967d/v1/analyze', headers=headers, params=params, data=data, auth=('apikey', 'pDqahAuneL2ZKLAoEmxTMeOWhJKWcx75MHq3Kx1AdLvk'))
    result = res.json()
    print(result)
    return find_insurance(result)

def find_insurance(nlp_res):
    for item in nlp_res["sentiment"]["targets"]:
      print(item)
      if item["text"] == "insurance":
        print("it got insurances")
        return True
    return False