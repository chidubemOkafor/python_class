import requests

url = "https://api-customer-038j.onrender.com/customer/"

put_response = requests.put(
    url + "2/", {"name": "mike", "age": "44", "order": "bread"})
print(put_response.json())

get_response = requests.get(url)
print(get_response.json())

post_response = requests.post(
    url, {"name": "daniel", "age": 29, "order": "rice"})
print(post_response.json())
