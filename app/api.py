import adal
from .models import *
import requests

# Id's
connectionId       = "1"
ledgerId           = "1"
workflowId         = "2"
contractCodeId     = "2"
workflowFunctionId = "5"

def get_api_headers():
    a_url = azure_key.objects.get(name="a_url").key
    client_secret = azure_key.objects.get(name="client_secret").key
    client_id = azure_key.objects.get(name="client_id").key
    context = adal.AuthenticationContext(a_url,api_version=None)
    token = context.acquire_token_with_client_credentials(client_id,client_id,client_secret)
    headers = {
        'Authorization' : "Bearer " + token['accessToken'],
    }
    return headers

def get_api_url(api_url):
    base_url = "https://codefundo-oz5vuz-api.azurewebsites.net/api/v2/"
    return base_url + api_url

def get_connection_and_ledger_id():
    r = requests.get(url=get_api_url("ledgers/connections/"),headers=get_api_headers())
    return r.json()

def check_canCreateContract():
    api_url = "capabilities/canCreateContract/" + workflowId + "/"
    r = requests.get(url=get_api_url(api_url),headers=get_api_headers())
    return r.json()

def submit_application(aadhar):
    post_data = {
        "workflowFunctionId" : workflowFunctionId,
        "workflowActionParameters":[{
            "name": "aadhar",
            "value": aadhar
        }]
    }
    api_url = "contracts?workflowId=" + workflowId + "&contractCodeId=" + contractCodeId + "&connectionId=" + connectionId
    headers = get_api_headers()
    headers['Content-Type'] = 'application/json;charset=utf-8'
    r = requests.post(url=get_api_url(api_url),headers=headers,json=post_data)
    return r.json()