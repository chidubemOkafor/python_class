import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.post(
    url, {"userId": 20, "title": "do assignment", "completed": "True"})
res = requests.get(url)
# print(res.status_code)
print(res.json())
