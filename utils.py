# Modul: utils
# Date: 04.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Some core utils, like log json in file.

import json
from os import path
import time
import logging

debugLogFilePath = "log/" + time.strftime("%Y%m%d") + "Debug.log"
debugLogFile=open(debugLogFilePath, 'a')
#loggingMode = 0 : none
#loggingMode = 1 : print log messages to logfile
#loggingMode = 2 : print log essage to console
#loggingMode = 3 : both
loggingMode = 0

def logRequestResponse(jsonData): #Logs the given jsonData in a logfile
                                  #with a timestamp in the filename.
    filePath = "log/" + time.strftime("%Y%m%d-%H%M%S") + "Request.log"
    with open(filePath, 'w') as file:
        json.dump(jsonData, file, indent=4, sort_keys=True)
        
def logMessage(message):
    if loggingMode == 3:
        print(message)
        print(message, file=debugLogFile)        
    if loggingMode == 2:
        print(message)
    elif loggingMode == 1:
        print(message, file=debugLogFile)
    else:
        return