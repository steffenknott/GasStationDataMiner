# Modul: utils
# Date: 04.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Some core utils, like log json in file.

import json
from os import path
import time

def logRequestResponse(jsonData): #Logs the given jsonData in a logfile
                                  #with a timestamp in the filename.
    filePath = "log/" + time.strftime("%Y%m%d-%H%M%S") + ".log"
    with open(filePath, 'w') as file:
        json.dump(jsonData, file, indent=4, sort_keys=True)