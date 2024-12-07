from __future__ import print_function
import time
import swagger_client
import swagger_client.configuration
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
conf = swagger_client.Configuration()
conf.host = '127.0.0.1:8000'

api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(conf))
id  = 1

try:
    # Init
    api_response = api_instance.init_init_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->init_init_get: %s\n" % e)
