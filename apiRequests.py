# Modul: requests
# Date: 03.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do detail- or list-requests on the tankerkoenig api.

import requests
import json

detailRequestOk = False

def DETAIL_REQUEST_URL():
    return "https://creativecommons.tankerkoenig.de/json/detail.php"
    
def LIST_REQUEST_URL():
    return "https://creativecommons.tankerkoenig.de/json/list.php"

def getApiKey():
    print("Start Reading Api Key")
    file = open('api.key')
    for line in file:
        fields = line.strip().split()
        print("Reading Api Key done")
        return fields[0]

def detailRequest(gasStationId):    #request detail information for a gasstation
    #try:
        print("Building parameter for detail request")
        payload = {'id': gasStationId, 'apikey': getApiKey()}
        print(payload)
        print("Requesting details in progress...")
        response = requests.get(DETAIL_REQUEST_URL(), params=payload)
        if response.ok:
            return response.json()
        else:
            print("Resonse was not ok.")
            return None
        
def listRequest(lat, lng, rad, sort, type): #request nearby gasstations
    print("Building paraneter for list request")
    payload = {'lat': lat, 'lng': lng,'rad': rad,'sort': sort,'type': type, 'apikey': getApiKey()}    
    print("Requesting nearby list")
    return requests.get(LIST_REQUEST_URL(), params=payload).json()
    
def getDetailRequestWasOk():
    return detailRequestOk


