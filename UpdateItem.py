import requests

url = "http://www.arcgis.com/sharing/rest/content/users/{{username}}/items/{{item_id}}/update"

payload = 'id=%7B%7Bitem_id%7D%7D&f=json&token=%7B%7Btoken%7D%7D&title=New%20title'
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
