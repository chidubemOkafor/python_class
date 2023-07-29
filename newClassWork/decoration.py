def Hello(test):

    if test() == "red":
        return test
    else:
        return test


@Hello
def say_somethingelse():
    return "Green"


@Hello
def say_something():
    return "Red"


a = say_something()
b = say_somethingelse()
print(a)
print(b)
