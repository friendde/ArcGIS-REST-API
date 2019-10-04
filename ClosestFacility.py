import requests

url = "http://route.arcgis.com/arcgis/rest/services/World/ClosestFacility/NAServer/ClosestFacility_World/solveClosestFacility?f=json&returnDirections=true&returnFacilities=false&returnIncidents=false&returnBarriers=false&returnPolylineBarriers=false&returnCFRoutes=true&useHierarchy=false&defaultCutoff=7&outSR=102100&travelMode=null&incidents=%7B%22type%22%3A%22features%22%2C%22features%22%3A%5B%7B%22geometry%22%3A%7B%22x%22%3A-13625563.00086767%2C%22y%22%3A4549045.33719256%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%5D%2C%22doNotLocateOnRestrictedElements%22%3Atrue%7D&facilities=%7B%22type%22%3A%22features%22%2C%22features%22%3A%5B%7B%22geometry%22%3A%7B%22x%22%3A-13625960%2C%22y%22%3A4549921%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%2C%7B%22geometry%22%3A%7B%22x%22%3A-13626184%2C%22y%22%3A4549247%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%2C%7B%22geometry%22%3A%7B%22x%22%3A-13626477%2C%22y%22%3A4549415%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%2C%7B%22geometry%22%3A%7B%22x%22%3A-13625385%2C%22y%22%3A4549659%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%2C%7B%22geometry%22%3A%7B%22x%22%3A-13624374%2C%22y%22%3A4548254%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%2C%7B%22geometry%22%3A%7B%22x%22%3A-13624891%2C%22y%22%3A4548565%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D%5D%2C%22doNotLocateOnRestrictedElements%22%3Atrue%7D&token={{token}}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
