# Modul: dataMiner
# Date: 13.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>, Eugen Geist
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

def addStationsInLocationToDb(lat, lng, rad):
    utils.logMessage("Requesting station list for lat: " + "{:.9f}".format(lat) + "long: " + "{:.9f}".format(lng) +  " and rad: " + "{:.9f}".format(rad))
    #Get Station data
    stationList = apiRequests.listRequest(lat, lng, rad)["stations"]
    dbHandle = connectDb.connect()
    if dbHandle is None:
        utils.logMessage("Connect DB - returned handle is null")
        sys.exit("Cannot connect to db.")
    for station in stationList:
        #Format for Database
        utils.logMessage("Preparing data of " + station["name"] + " for insertion")
        station["_id"] = station["id"]
        del station["id"]
        del station["dist"]
        del station["price"]
        utils.logMessage("Inserting station data of " + station["name"] + " to db")
        try:
            #If data for this station already exists replace, else insert
            dbHandle.stations.replace_one({"_id" : station["_id"]},  station, upsert=True)
            utils.logMessage("Station " + station["name"] + " added")
        except Exception as exc:
            utils.logMessage("Exception while inserting station data in db: %s " %exc)
            raise SystemExit
    
    
    
    


if __name__ == "__main__":

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
            utils.logMessage("Getting details for stationId = " + i["_id"])
            detailRequestResult = apiRequests.detailRequest(i["_id"])
            if detailRequestResult is not None:
                #build and add generally data to filtered result dict
                filteredResult = dict()
                filteredResult["dateTime"] = datetime.datetime.now()
                filteredResult["stationId"] = i["_id"]
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
        
        
