import requests
import json 

a = input("Please input something==>")
url = "https://api.languagetool.org/v2/check"

data = {
    'text' : f"{a} ",
    'language' : 'auto'
}
response = requests.post(url, data=data)
result = json.loads(response.text)
print(result['matches'][0]['replacements'])
