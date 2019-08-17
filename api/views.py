import requests
from django.http import JsonResponse
import json
from app import api
def testView(request):
    # r = requests.get(api.get_api_url("contracts/?workflowId=2"),headers=api.get_api_headers())
    r = requests.get(api.get_api_url("applications/workflows/2/"),headers=api.get_api_headers())
    return JsonResponse(r.json(),safe=False)
