import requests

url = "https://www.arcgis.com/sharing/rest/community/signup"

payload = {'username': '{{username}}',
'password': '{{password}}',
'email': '{{email}}',
'firstName': 'John',
'lastName': 'Doe',
'securityQuestionIdx': '5',
'securityAnswer': 'Lorem ipsum dolor',
'provider': 'arcgis',
'usertype': 'both',
'referer': 'arcgis.com',
'f': 'json'}
files = {}
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
