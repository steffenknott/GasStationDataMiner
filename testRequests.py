# Modul: requests
# Date: 03.07.2015
# Author: dtonal - Torben Mueller <dtonal@posteo.de>
# Summary: Modul to do first request testing.
import apiRequests
import utils

import requests
import json

print("Testing detail request for gasstation with fix id")
jsonData=apiRequests.detailRequest("e6aaa4e0-5876-4e05-a564-fb949df831e7")
print("Requesting details finished.")
if jsonData is None:
    print("Error while requesting details.")
else:
    print("Requesting details succeded.")
    utils.logRequestResponse(jsonData)
    
print("Testing list request for gasstation with fix parameters")
jsonData=apiRequests.listRequest("53.223546", "10.169761", "10", "price", "diesel")
print("Requesting list finished.")
if jsonData is None:
    print("Error while requesting list.")
else:
    print("Requesting list succeded.")
    utils.logRequestResponse(jsonData)
    