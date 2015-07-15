# Modul: apiRequests
# Date: 03.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do detail- or list-requests on the tankerkoenig api.

import requests
import json
import doctest
import utils

detailRequestOk = False

def DETAIL_REQUEST_URL():
    return "https://creativecommons.tankerkoenig.de/json/detail.php"
    
def LIST_REQUEST_URL():
    return "https://creativecommons.tankerkoenig.de/json/list.php"

def getApiKey():
    """" 
    >>>getApiKey.len() > 0
    False
    >>>
    """
    utils.logMessage("Start Reading Api Key")
    file = open('api.key')
    for line in file:
        fields = line.strip().split()
        utils.logMessage("Reading Api Key done")
        return fields[0]

def detailRequest(gasStationId):
    try:
        utils.logMessage("Building parameter for detail request")
        payload = {'id': gasStationId, 'apikey': getApiKey()}
        utils.logMessage(payload)
        utils.logMessage("Requesting details in progress...")
        response = requests.get(DETAIL_REQUEST_URL(), params=payload)
        if response.ok:
            return response.json()
        else:
            utils.logMessage("Response was not ok.")
            return None
    except Exception as exc:
        raise
        
def listRequest(lat, lng, rad, sort, type): #request nearby gasstations
    try:
        utils.logMessage("Building paraneter for list request")
        payload = {'lat': lat, 'lng': lng,'rad': rad,'sort': sort,'type': type, 'apikey': getApiKey()}    
        utils.logMessage("Requesting nearby list")
        response = requests.get(LIST_REQUEST_URL(), params=payload)
        if response.ok:
            return response.json()
        else:
            utils.logMessage("Response was not ok.")
            return None
    except Exception as exc:
        raise
    
def getDetailRequestWasOk():
    return detailRequestOk
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()


