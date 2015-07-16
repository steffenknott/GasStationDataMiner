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

utils.loggingMode=0

try:
    utils.logMessage("Start mining at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
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
    #Getting a list of all stations in in the db
    stations= dbHandle.stations.find()
    for i in stations:
        #iterate trough all stations and do a detailRequest
        utils.logMessage("Getting details for stationId = " + i["id"])
        detailRequestResult = apiRequests.detailRequest(i["id"])
        if detailRequestResult is not None:
            #build and add generally data to filtered result dict
            filteredResult = dict()
            filteredResult["dateTime"] = datetime.datetime.now()
            filteredResult["stationId"] = i["id"]
            if "diesel" in detailRequestResult["station"]:
                #create a diesel price document
                filteredResult["price"] =  detailRequestResult["station"]["diesel"]
                dbHandle.dieselPrices.insert_one(filteredResult)
                utils.logMessage("diesel added")
            if "e5" in detailRequestResult["station"]:
                #reuse diesel price document for e5 doc
                filteredResult["price"] =  detailRequestResult["station"]["e5"]
                dbHandle.e5Prices.insert_one(filteredResult)
                utils.logMessage("e5 added")
            if "e10" in detailRequestResult["station"]:
                #reuse e5 price document for e10 doc
                filteredResult["price"] =  detailRequestResult["station"]["e10"]
                dbHandle.e10Prices.insert_one(filteredResult)
                utils.logMessage("e10 added")
    utils.logMessage("Finished mining at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
except Exception as exc:
        utils.logMessage("Exception while tupdate data in db: %s " %exc)
        raise SystemExit
    
    
