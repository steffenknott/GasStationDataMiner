 Modul: pricesToInflux
# Date: 24.04.2018
# Author: steffenknott - Steffem Knott
# Summary: Modul to fetch prices and push then into an InfluxDB instance.
import apiRequests
import utils

import requests
import json
import doctest

utils.loggingMode=3

with open('tankstellen.conf','r') as stations:
  for station in stations:
    try:
        utils.logMessage("Fetching station")
        jsonData=apiRequests.detailRequest(station.rstrip())
        if jsonData is None:
            utils.logMessage("Error while requesting details.")
        else:
            utils.logMessage("Requesting details succeded.")
            with open('sorten.conf','r') as sorten:
                for sorte in sorten:
                    dbquery= '{}={}'.format(sorte.rstrip(), jsonData["station"][sorte.rstrip()])
                    print(dbquery)
                    utils.logRequestResponse(jsonData)
    except Exception as exc:
            utils.logMessage("Exception while testing Requests: ", exc)
            raise SystemExit
