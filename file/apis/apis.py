import requests

response = requests.get("http://api.publicapis.org/entries")
res = response.json()
print()
print("What are you looking for?")
print("1. Link")
print("2. Description")
print("3. Category")
print()
number = int(input("Write a number: "))
length = range(len(res["entries"]))
na = []


class State:
    def __init__(self, number):
        self.number = number
        if self.number == 1:
            self.value = "Link"
        elif self.number == 2:
            self.value = "Description"
        elif self.number == 3:
            self.value = "Category"
        else:
            self.value = "API"

    def getValue(self):
        return self.value


if number == 1:
    name = input("Enter API name: ")

    for i in length:
        query = res["entries"][int(i)]["API"]
        if name == query:
            na.append(res["entries"][int(i)]["Link"])


print(na)
