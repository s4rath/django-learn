import requests

endpoint ="http://127.0.0.1:8000/api/products/1/update/"
# endpoint ="https://httpbin.org/anything"

data={
    'title':"Hello world",
    'price':0.67
}

get_response = requests.put(endpoint,json=data)
# print(get_response)
print(get_response.json())
