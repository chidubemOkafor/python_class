import random

def generatePassword():
    num = int(input("what length should the password be: "))
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    special_characters = '!@#$%^&🗣*()?+~`_😆'
    password = []
    for _ in range(num):
        our_choice = [random.choice(special_characters),str(random.randrange(0,9)), random.choice(lower_case), random.choice(upper_case)]
        password.append(random.choice(our_choice))
    new_password1 = "".join(password)
    with open("hidden_key.txt", "w+") as file:
        file.write(new_password1)
        file.seek(0)
    print(file.read())

generatePassword()