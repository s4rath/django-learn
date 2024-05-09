import requests
from getpass import getpass

password=getpass()
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
# endpoint ="https://httpbin.org/anything"


auth_response = requests.post(auth_endpoint,json={'username':'cfe','password':password})
# print(get_response)
print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        "Authorization": f'Bearer {token}'
    }
    endpoint = "http://127.0.0.1:8000/api/products/"
    # endpoint ="https://httpbin.org/anything"


    get_response = requests.get(endpoint,headers=headers)
    # print(get_response)
    print(get_response.json())

    print(get_response.status_code)

