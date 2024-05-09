import requests

endpoint ="http://127.0.0.1:8000/api/products/"
# endpoint ="https://httpbin.org/anything"
headers={'Authorization': 'Bearer 03ba39b314e45d2ef57c543d8c7f94c401813589'}

data={
    'title':'mobile'
}
get_response = requests.post(endpoint,json=data,headers=headers)
# print(get_response.content)
print(get_response.json())

