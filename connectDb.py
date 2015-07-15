# Modul: connectDb
# Date: 13.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to connect to a mongo db instance.

import sys
import utils

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect(dbHost = "localhost", dbPort = 27017, dbName = "euto"):
    """ Connect to MongoDB """
    try:
        c = MongoClient(dbHost, dbPort)
        utils.logMessage("Connected successfully")
    except ConnectionFailure as e:
        utils.logMessage("Could not connect to MongoDB: %s" % e)
        return null
    # getting a datebase handle to the db
    return c.euto   
    
if __name__ == "__main__":
    connect()


