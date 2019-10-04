import requests

url = "http://www.arcgis.com/sharing/rest/content/users/{{username}}/addItem"

payload = 'type=Web%20Mapping%20Application&typeKeywords=Web%20Map%2C%20Map%2C%20Online%20Map%2C%20Mapping%20Site%2C%20JavaScript%2C%20Ready%20To%20Use%20%2CselfConfigured&thumbnailURL=http%3A//static.arcgis.com/images/webapp.png&item=Servicios%20Sanitarios%20de%20Galicia99&title=Servicios%20Sanitarios%20de%20Galicia99&tags=servicios%2Csanitarios%2Cgalicia&snippet=&wabType=HTML&sharing=false&webMapId=5855a4382c1a4148bbd329b0515332a0&shareWithWebMap=true&text=%7B%22source%22%3A%22931653256fd24301a84fc77955914a82%22%2C%22folderId%22%3Anull%2C%22values%22%3A%7B%22webmap%22%3A%225855a4382c1a4148bbd329b0515332a0%22%7D%7D&f=json&token=%7B%7Btoken%7D%7D&url=http%3A//%7B%7Busername%7D%7D.maps.arcgis.com/apps/GeoForm/index.html'
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
