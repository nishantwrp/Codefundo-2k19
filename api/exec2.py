import adal
import requests

a_url = "https://login.microsoftonline.com/codefundo19outlook.onmicrosoft.com/"
# client_secret = "AmC0vkje*[Ri1.EXKH1/WL0B4dSOW]E]"
client_id = "d70d6f47-9d28-496e-b7dc-cbf8d03e68d7"
context = adal.AuthenticationContext(a_url,api_version=None)
token = context.acquire_token_with_username_password(resource=client_id,username="codefundo19@outlook.com",password="/data/study_material",client_id=client_id)
print(token['accessToken'])
# base_url = "https://codefundo-oz5vuz-api.azurewebsites.net/api/v1/"

# api_url = "/users/me/"
# url = base_url + api_url
# headers = {
#     'Authorization' : "Bearer " + token['accessToken'],
#     'Content-Type': 'application/json-patch+json',
# }
# data = {
#   "userId": 2,
#   "applicationRoleId": 3
# }
# r = requests.get(url=url,headers=headers)
# print(r)
# try:
#     print(r.content)
#     print(r.json())
# except:
#     pass
