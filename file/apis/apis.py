import requests


class State:
    def __init__(self, number):
        self.number = number
        if self.number == 1:
            self.value = "Link"
        elif self.number == 2:
            self.value = "Description"
        elif self.number == 3:
            self.value = "Category"
        elif self.number == 4:
            self.value = "Auth"
        else:
            self.value = "API"

    def getValue(self):
        return self.value


response = requests.get("http://api.publicapis.org/entries")
res = response.json()
print()
print("What are you looking for?")
print("1. Link")
print("2. Description")
print("3. Category")
print("4. auth")
print()
number = int(input("Write a number: "))
length = range(len(res["entries"]))
na = ""

state = State(number)
if number in [1, 2, 3, 4]:
    name = input("Enter API name: ")

    for i in length:
        query = res["entries"][i]["API"]
        if name == query:
            na = res["entries"][i][state.getValue()]
            break  # Exit the loop since we found a match
        else:
            na = "Link does not exist"

print(na)
