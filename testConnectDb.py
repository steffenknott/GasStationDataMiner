# Modul: testConnectDb
# Date: 13.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do first request testing.
import connectDb
import utils

utils.loggingMode=1

try:
    utils.logMessage("Testing DB Connection")
    dbHandle = connectDb.connect()
    if dbHandle is None:
        utils.logMessage("Connect DB - returned handle is null")
    else:
        utils.logMessage("Connect DB - getting handle successfully")
except Exception as exc:
        utils.logMessage("Exception while testing connectDb: %s " %exc)
        raise SystemExit
    
    

