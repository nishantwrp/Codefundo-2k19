from django.shortcuts import render
import adal
import requests
from django.http import JsonResponse
from app.api import *
import json
def testView(request):
    base_url = "https://codefundo-oz5vuz-api.azurewebsites.net/api/v2/"
    api_url = "capabilities/canCreateContract/2/"
    url = "https://codefundo-oz5vuz-api.azurewebsites.net/api/v2/contracts?workflowId=2&contractCodeId=2&connectionId=1"
    # url = base_url + api_url
    headers = {
        # 'Authorization' : "Bearer " + azure_key.objects.get(name="bearer_token").key,
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCIsImtpZCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCJ9.eyJhdWQiOiJkNzBkNmY0Ny05ZDI4LTQ5NmUtYjdkYy1jYmY4ZDAzZTY4ZDciLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kMzE4YzZmYi0wMzc2LTRkYmYtOTAyMi0yODJjMzg4ODM4MGYvIiwiaWF0IjoxNTY1ODY2MzM2LCJuYmYiOjE1NjU4NjYzMzYsImV4cCI6MTU2NTg3MDIzNiwiYWlvIjoiQVZRQXEvOE1BQUFBTGx2ZWRsNnRiYVlOWkJMMnVCKzJxU2lWQzF6eE9JUThBNC9zTWZFNCtmUndRZHR4ZktzS040UlVjQ0xmcGlLZVhETVl6VjZJOUVJby9iTktxd2VKTG5VTVEzcDBmRHhPOHNUTnJGc1VrT3M9IiwiYW1yIjpbInB3ZCJdLCJjX2hhc2giOiJrVmstbVpHalhDUUdYaTQtQkZwZGtnIiwiZW1haWwiOiJjb2RlZnVuZG8xOUBvdXRsb29rLmNvbSIsImZhbWlseV9uYW1lIjoiVGVhbSIsImdpdmVuX25hbWUiOiJDb2RlZnVuZG8iLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjE0LjEzOS4yMjguMjE2IiwibmFtZSI6IkNvZGVmdW5kbyBUZWFtIiwibm9uY2UiOiI2MmM5YzhlYy1iMWYzLTQ5NzYtYmE0Yi1lNzkxMWUzZWI2NjciLCJvaWQiOiI5NjkwMDEzYS1jZjFjLTQyODQtYTVhNy1lZmNjMGUxNDcyZDkiLCJyb2xlcyI6WyJBZG1pbmlzdHJhdG9yIl0sInN1YiI6IkR4T2wybnh5MUtCVXI2OTB1WDhhSjVRZ1NTQldPc0FwS2F1X0ktUVBEcm8iLCJ0aWQiOiJkMzE4YzZmYi0wMzc2LTRkYmYtOTAyMi0yODJjMzg4ODM4MGYiLCJ1bmlxdWVfbmFtZSI6ImxpdmUuY29tI2NvZGVmdW5kbzE5QG91dGxvb2suY29tIiwidXRpIjoiOHZOVUs2NWZNa3VWX19sakI0VUtBQSIsInZlciI6IjEuMCJ9.oCEWxCjbg2yBRxf2VgdZvEYGzNpI1-wO-gEurpCSSSsbQ0TUr0WfwYpI-acUodxKUcTWvbb2LQ0TVvcnSv9jI86MKeCjHX3MeD_63r0R9Ci8yH4PtnKQul0DgRMyXIh1OWTMeSWuCoCfp8Y6DMfJ0wNxsm7IJn6EdWxQ7R6vL369oCBUXQPL2s7Y7ZA76wl2RmR17nAjxra-HTko6rDIWQzHXVMCoZ3Bwg7ZCB-Wqrw10CjtB0cmHDuR0fFzU8Ye0jGre8sXqY8QYJEf3M459tk0LYYiqv5GnVkv9dAK5X5ZZIkHxOjPrAoNMAe3zfKh4bydW7SUjrurB5tDsidwPQ',
        'Content-Type': 'application/json;charset=utf-8',
    }
    x_data = {
        "workflowFunctionId":5,"workflowActionParameters":[{
        "name": "aadhar",
        "value": "5655"
    }]
    }
    abc = {
        "name": "aadhar",
        "value": "5655"
    }
    # abc_json = json.dumps(abc)
    x = list()
    x.append(abc)
    abc_json = json.dumps(x)
    data = {"workflowFunctionId":5,"workflowActionParameters":abc_json}
    # print(abc_json)
    # print(data)
    print(json.dumps(x_data))
    r = requests.post(url=url,headers=headers,json=x_data)
    print(r)
    print(r.content)
    return JsonResponse(r.json(),safe=False)
