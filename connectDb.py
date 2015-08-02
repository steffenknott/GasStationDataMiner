# Modul: connectDb
# Date: 13.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to connect to a mongo db instance.

import sys
import os
import logging
import logging.config

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.config.fileConfig('logging.conf')

def connect(dbHost = "192.168.2.5", dbPort = 27017, dbName = "euto"):
    logger = logging.getLogger('database')
    """ Connect to MongoDB """
    try:
        c = MongoClient(dbHost, dbPort)
        logger.info("Connected successfully")
    except ConnectionFailure as e:
        logger.exception("Could not connect to MongoDB.")
        return None
    # getting a datebase handle to the db
    return c.euto   
    
if __name__ == "__main__":
    connect()


