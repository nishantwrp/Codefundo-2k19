import adal
import requests

a_url = "https://login.microsoftonline.com/d318c6fb-0376-4dbf-9022-282c3888380f"
client_secret = "AmC0vkje*[Ri1.EXKH1/WL0B4dSOW]E]"
client_id = "d70d6f47-9d28-496e-b7dc-cbf8d03e68d7"
context = adal.AuthenticationContext(a_url,api_version=None)
token = context.acquire_token_with_client_credentials(client_id,client_id,client_secret)
base_url = "https://codefundo-oz5vuz-api.azurewebsites.net/api/v2/"

api_url = "/applications/3/roleAssignments/"
url = base_url + api_url
headers = {
    'Authorization' : "Bearer " + token['accessToken'],
    'Content-Type': 'application/json-patch+json',
}
# data = {
    
#         "externalID": "a8870184-1c0f-42a4-99d7-591c447538b1",
#         "firstName": "Nishant",
#         "lastName": "Mittal",
#         "emailAddress": "mittalnishant14@outlook.com"
      
# }
# files = {
#     'contractFile': open('LetsVoteBlockchain.sol','rb')
# }
params = {
    # 'top' : 10,
    # 'enabled': True,
    # 'skip': 0
}
# post_data = {
#         "workflowFunctionId" : 5,
#         "workflowActionParameters":[{
#             "name": "aadhar",
#             "value": "aadhar"
#         }]
# }
# api_url = "contracts?workflowId=" + "2" + "&contractCodeId=" + "2" + "&connectionId=" + "1"
# url = base_url + api_url
# headers['Content-Type'] = 'application/json;charset=utf-8'
post_data = {
  "userId": 2,
  "applicationRoleId": 4
}

r = requests.post(url=url,headers=headers,json=post_data)

print(r)
try:
    print(r.content)
    print(r.json())
except:
    pass
