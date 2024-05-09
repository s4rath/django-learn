import requests

endpoint ="http://127.0.0.1:8000/api/"
# endpoint ="https://httpbin.org/anything"


get_response = requests.post(endpoint,json={"content":"the title of product",'title':"chair",'price':89})
# print(get_response)
print(get_response.json())

print(get_response.status_code)

