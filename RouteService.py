import requests

url = "http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve?stops=-3.696715,40.436614;-3.673884,40.430277&f=json&token={{token}}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
