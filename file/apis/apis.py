import requests

response = requests.get("http://api.publicapis.org/entries")
res = response.json()

name = input("enter a name: ")
length = range(len(res["entries"]))
for i in length:
    if name == res["entries"][i]["API"]:
        print(name)
    else:
        print("name does not exist")
# if name in res["entries"][0]["Name"]:
#     print(name)
# print("no name")
# content = res["entries"][0]["name"]
# print(content)
