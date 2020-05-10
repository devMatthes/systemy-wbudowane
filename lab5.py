import requests, json, codecs

r = requests.get('http://api.open-notify.org/astros.json')
r.json()
response = r.text
with open('data.json', 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=4, ensure_ascii=False)