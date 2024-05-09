import requests

endpoint ="http://127.0.0.1:8000/api/products/1/"
# endpoint ="https://httpbin.org/anything"


get_response = requests.get(endpoint,)
# print(get_response)
print(get_response.json())

# print(get_response.status_code)

