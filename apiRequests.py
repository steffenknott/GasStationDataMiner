# Modul: apiRequests
# Date: 03.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do detail- or list-requests on the tankerkoenig api.
import os
import requests
import doctest
import logging
import logging.config

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.config.fileConfig('logging.conf')

detailRequestOk = False

LIST_REQUEST_URL = "https://creativecommons.tankerkoenig.de/json/list.php"
DETAIL_REQUEST_URL = "https://creativecommons.tankerkoenig.de/json/detail.php"
PRICES_REQUEST_URL = "https://creativecommons.tankerkoenig.de/json/prices.php"

def getApiKey():
    """" 
    >>>getApiKey.len() > 0
    False
    >>>
    """
    logger = logging.getLogger('apiRequests')
    logger.info("Start Reading Api Key")
    file = open('api.key')
    for line in file:
        fields = line.strip().split()
        logger.info("Reading Api Key done")
        return fields[0]


def detailRequest(gasStationId):
    '''Request detail information for a gasstation.

    Keyword arguments:
    gasStationId -- api id of the gasstation

    Returns: json or None

    '''
    logger = logging.getLogger('apiRequests')
    try:
        logger.info("Building parameter for detail request")
        payload = {'id': gasStationId, 'apikey': getApiKey()}
        #logger.debug("Payload: " + payload)
        logger.info("Requesting details in progress...")
        logger.info("url: " + DETAIL_REQUEST_URL)
        logger.info("payload.id: " + payload["id"])
        logger.info("payload.apikey: " + payload["apikey"])
        response = requests.get(DETAIL_REQUEST_URL, params=payload)
        logger.info("request done")
        if response.ok:
            return response.json()
        else:
            logger.error("Response was not ok.")
            return None
    except Exception as exc:
        logger.exception("Exception when requesting details for station with id " + gasStationId)
        return None
        
def listRequest(lat, lng, rad, sort="price", type="e10"):
    '''Request nearby gasstations.

    Keyword arguments:
    lat -- Latitude of location
    lng -- Longitude of location
    rad -- Radius of request
    sort -- 
    type --

    Returns:
     
    '''
    logger = logging.getLogger('apiRequests')
    try:
        logger.info("Building parameter for list request")
        payload = {'lat': lat, 'lng': lng,'rad': rad,'sort': sort,'type': type, 'apikey': getApiKey()}    
        logger.info("Requesting nearby list")
        response = requests.get(LIST_REQUEST_URL, params=payload)
        if response.ok:
            return response.json()
        else:
           logger.error("Response was not ok.")
           return None
    except Exception as exc:
        logger.exception("Exception when requesting nearby stations.")
        return None


def detailRequest(gasStationIds):
    '''Request prices for up to 10 gasstations.

    Keyword arguments:
    gasStationIds -- comma-separated list of api ids of gasstations (max 10)

    Returns: json or None

    '''
    logger = logging.getLogger('apiRequests')
    try:
        logger.info("Building parameter for prices request")
        payload = {'ids': gasStationIds, 'apikey': getApiKey()}
        #logger.debug("Payload: " + payload)
        logger.info("Requesting prices in progress...")
        logger.info("url: " + PRICES_REQUEST_URL)
        logger.info("payload.ids: " + payload["ids"])
        logger.info("payload.apikey: " + payload["apikey"])
        response = requests.get(DETAIL_REQUEST_URL, params=payload)
        logger.info("request done")
        if response.ok:
            return response.json()
        else:
            logger.error("Response was not ok.")
            return None
    except Exception as exc:
        logger.exception("Exception when requesting prices for station with id " + gasStationId)
        return None
    
def getDetailRequestWasOk():
    return detailRequestOk
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()


