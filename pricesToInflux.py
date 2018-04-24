# Modul: pricesToInflux
# Date: 24.04.2018
# Author: steffenknott - Steffem Knott
# Summary: Modul to fetch prices and push then into an InfluxDB instance.
import apiRequests
import utils

import requests
import json
import doctest

from influxdb import InfluxDBClient

utils.loggingMode=3
client = InfluxDBClient("10.0.0.21", 8086, "", "", "consumption")

with open('tankstellen.conf','r') as stations:
  for station in stations:
    try:
        #utils.logMessage("Fetching station")
        jsonData=apiRequests.detailRequest(station.rstrip())
        if jsonData is None:
            utils.logMessage("Error while requesting details.")
        else:
            #utils.logMessage("Requesting details succeded.")
            with open('sorten.conf','r') as sorten:
                json_body = [
                {
                    "measurement": "spritpreise",
                    "tags": {
                        "tankstelle": station.rstrip()
                    },
                    "fields": {
                    }
                }
                ]
                for sorte in sorten:
                    if sorte.rstrip() in jsonData["station"]:
                        json_body[0]['fields'].update({sorte.rstrip(): jsonData["station"][sorte.rstrip()]})
                print("INSERT JSON: {0}".format(json_body))
                client.write_points(json_body)
                 #       utils.logRequestResponse(jsonData)
    except Exception as exc:
            utils.logMessage("Exception while testing Requests: ", exc)
            raise SystemExit
