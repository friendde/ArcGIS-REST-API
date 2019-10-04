import requests

url = "http://www.arcgis.com/sharing/rest/content/items/{{item_id}}/share"

payload = 'f=json&everyone=true&org=false&groups=&items=%7B%7Bitem_id%7D%7D&token=%7B%7Btoken%7D%7D'
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
