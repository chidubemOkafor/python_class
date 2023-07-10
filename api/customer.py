import requests

url = "https://api-customer-038j.onrender.com/customer/"

print("what do you want to do?")
print("1. update_order")
print("2. add_order")
print("3. get orders")
print("4. get with id")
print("5. delete")
print()
number = int(input("write a number: "))

if number == 1:
    id = int(input("what is your id: "))
    name = input("name: ")
    age = int(input("age: "))
    order = input("order: ")
    print()
    put_response = requests.put(
        url + f"{id}/", {f"name": {name}, "age": {age}, "order": {order}})
    print(put_response.json())

if number == 2:
    name = input("name: ")
    age = int(input("age: "))
    order = input("order: ")
    print()
    post_response = requests.post(
        url, {f"name": {name}, "age": {age}, "order": {order}})
    print(post_response.json())

if number == 3:
    get_response = requests.get(url)
    print(get_response.json())

if number == 4:
    id = int(input("id of what you want to get"))
    get_response = requests.get(url + f"{id}/")

if number == 5:
    id = int(input("id of what you want to delete: "))
    get_response = requests.delete(url + f"{id}/")
