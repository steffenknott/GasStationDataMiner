# Modul: dataMiner
# Date: 13.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do first request testing.
import apiRequests
import utils
import sys
import connectDb
import datetime

import requests
import json
import doctest

utils.loggingMode=3

try:
    utils.logMessage("Establishing DB connection")
    dbHandle = connectDb.connect()
    if dbHandle is None:
        utils.logMessage("Connect DB - returned handle is null")
        sys.exit("Cannot connect to db.")
    utils.logMessage("Connect DB - getting handle successfully")
except Exception as exc:
        utils.logMessage("Exception while testing connectDb: %s " %exc)
        raise SystemExit

try:
    jsonData=apiRequests.listRequest("53.223546", "10.169761", "25", "price", "diesel")
    stations= jsonData["stations"]
    for i in stations:
        #utils.logMessage("Update gas station %s ( %s in %s)" i["id"] i["brand"] i["place"])
        i["lastUpdate"]=datetime.datetime.now()
        dbHandle.stations.update({'id':i["id"]}, i)
        jsonData=apiRequests.detailRequest(i["id"])
        pricingData = 
        dbHandle.i["id"]
except Exception as exc:
        utils.logMessage("Exception while tupdate data in db: ", exc)
        raise SystemExit
    
    