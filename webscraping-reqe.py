import requests


url = 'https://www.tabnak.com'
req = requests.get(url)
print(req.status_code)
#print(req.headers)
session = requests.session()
print(session.get(url).content)

