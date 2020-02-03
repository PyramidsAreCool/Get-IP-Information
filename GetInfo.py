import requests
import json

# Starting Print text

print("-------IP Information-------")

iprequest = requests.get("https://api.ipify.org/?format=json")

ipjson = json.loads(iprequest.text)

ipinforequest = requests.get("http://ip-api.com/json/" + ipjson["ip"])

ipinfojson = json.loads(ipinforequest.text)

print("IP: " + ipjson["ip"])

print("IP Country: " + ipinfojson["country"])

print("IP Country Code: " + ipinfojson["countryCode"])

print("IP Region: " + ipinfojson["region"])

print("IP Region Name: " + ipinfojson["regionName"])

print("IP City: " + ipinfojson["city"])

print("IP Zip: " + ipinfojson["zip"])

print("IP Lat: ", ipinfojson["lat"])

print("IP Lon: ", ipinfojson["lon"])

print("IP Timezone: " + ipinfojson["timezone"])

print("IP ISP: " + ipinfojson["isp"])

print("IP Org: " + ipinfojson["org"])

print("IP As: " + ipinfojson["as"])

# End Print Text

print("----------------------------")
