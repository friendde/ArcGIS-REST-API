import requests

url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/geocodeAddresses?addresses={     \"records\": [         {             \"attributes\": {                 \"OBJECTID\": 1,                 \"Address\": \"Calle elena\",                 \"City\": \"Granada\"            }         },         {             \"attributes\": {                 \"OBJECTID\": 2,                 \"Address\": \"Emilio Muñoz 35\",                 \"City\": \"Madrid\",                 \"Region\": \"CA\",                 \"Postal\": \"28037\"             }         }     ] }&sourceCountry=ES&token={{token}}&f=pjson"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
