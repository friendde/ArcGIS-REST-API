import requests

url = "https://www.arcgis.com/sharing/rest/community/checkUsernames"

payload = {'usernames': '{{username}}',
'f': 'json'}
files = {}
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
