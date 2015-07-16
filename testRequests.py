# Modul: testRequests
# Date: 03.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do first request testing.
import apiRequests
import utils

import requests
import json
import doctest

utils.loggingMode=3

try:
    utils.logMessage("Testing detail request for gasstation with fix id")
    jsonData=apiRequests.detailRequest("8f9a684e-975d-4856-9eb9-9cc14d241b7b")
    print(type(jsonData))
    utils.logMessage("Requesting details finished.")
    if jsonData is None:
        utils.logMessage("Error while requesting details.")
    else:
        utils.logMessage("Requesting details succeded.")
        utils.logRequestResponse(jsonData)
        
    utils.logMessage("Testing list request for gasstation with fix parameters")
    jsonData=apiRequests.listRequest("53.223546", "10.169761", "10", "price", "diesel")
    utils.logMessage("Requesting list finished.")
    if jsonData is None:
        utils.logMessage("Error while requesting list.")
    else:
        utils.logMessage("Requesting list succeded.")
        utils.logRequestResponse(jsonData)
except Exception as exc:
        utils.logMessage("Exception while testing Requests: ", exc)
        raise SystemExit