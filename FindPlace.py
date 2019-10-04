import requests

url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find"

payload = 'text=Calle%20emilio%20mu%F1oz%2035%2C%20Madrid&categorforStoragey=true&outFields=*&f=pjson&token=%7B%7Btoken%7D%7D'
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
