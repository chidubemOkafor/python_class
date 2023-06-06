def my_function():
    print("hello from a function")

my_function()

def sum():
    print(5+5)

sum()

def sum2(a,b,c):
    print(a+b+c)

sum2(1,2,3)


def name_of_people(*args):
    print(args)
    for name in args:
        print(name)

name_of_people("john")

def name_of_persons(name,age):
    print(f"hi i'm {name}, and i'm {age} years old")

name_of_persons(age=27, name='john')

def Profile(name,age,salary=50000): 
    print(f"{name} is {age} years old and he works in the factory, with {salary}")

Profile("john", 29, 1000000)

#passing a list as an argument
def profile(list_of_names):
    for names in list_of_names:
        print(names)

profile(["james","mum","dad","dubem"]) #list
profile(("name","age","dad","home")) #turple
profile("this is a random name that is not the same as you would tell") #string

def name_of_age(age):
    if age > 10:
        return "you are old enough"
    else:
        return "too young for this"

response = name_of_age(20)
print(response)

#recursion
def sum(a, b):
    print(a,b)
    a -= 1
    if a > 0:
        sum(a,b)

sum(9,2)