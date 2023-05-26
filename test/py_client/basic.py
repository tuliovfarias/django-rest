import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

# get_response = requests.get(endpoint, params={"product_id":123}, json={"query":"test_query"})
get_response = requests.get(endpoint)
get_response = requests.post(endpoint, json={"title":"Title3"})
print(get_response.json())
print(get_response.status_code)

