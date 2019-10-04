import requests

url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?token={{token}}&f=pjson&location=-3.626966,40.432546"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
