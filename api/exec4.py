from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_id = '2' # str | The id of the application.

try:
    # 
    api_instance.application_get(application_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->application_delete: %s\n" % e)
