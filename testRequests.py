import apiRequests
import requests
import json

print("Testing detail request for gasstation with fix id")
jsonData=apiRequests.detailRequest("e6aaa4e0-5876-4e05-a564-fb949df831e7").json()
dataString = json.dumps(jsonData, indent=4)
resp_dict = json.loads(dataString)
print("brand" , resp_dict['station']['brand'])
print("name" , resp_dict['station']['name'])
print("place" , resp_dict['station']['place'])
print("isOpen" , resp_dict['station']['isOpen'])
print("diesel" , resp_dict['station']['e5'])
print("e5" , resp_dict['station']['e5'])
print("e10" , resp_dict['station']['e5'])