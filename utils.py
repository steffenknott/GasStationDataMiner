# Modul: utils
# Date: 04.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Some core utils, like log json in file.

import json
import os
import time
import logging

debugLogFilePath = "log/" + time.strftime("%Y%m%d") + "Debug.log"
debugLogFile=open(debugLogFilePath, 'a')
#loggingMode = 0 : none
#loggingMode = 1 : print log messages to logfile
#loggingMode = 2 : print log essage to console
#loggingMode = 3 : both
loggingMode = 0

        
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

def logRequestResponse(jsonData): 
    '''Logs jsonData in a logfile with a timestamp in the filename.

    Keyword arguments:
    jsonData -- data which is logged

    Returns: None

    '''
    filePath = "log/" + time.strftime("%Y%m%d-%H%M%S") + ".log"
    if not os.path.exists(os.path.dirname(filePath)):
        os.makedirs(os.path.dirname(filePath))
    with open(filePath, 'w+', encoding='utf-8') as file:
        json.dump(jsonData, file, indent=4, sort_keys=True, ensure_ascii=False)

