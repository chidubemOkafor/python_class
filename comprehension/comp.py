# nums = [1,3,4,5,7,8,9,90]
# nums3 = [33,4,5,6,7,8,9,9,9,9]


# num2 = [(n * 8) for n in nums if n > 2]
# num3 = [(n) for n in nums3 if n in nums]
# print(num3)
# if there is an else statement start with the condition
# we have the list comprehension [i * 2 for i in ranger(10)]
# dictionary  {i: i * 2 for i in ranger(10)}
# set {i * 2 for i in ranger(10)}

# a = [1,2,3,4,5,6,7,8,9,10]
# b = [2,4,6,8,10,12,14,16,18,20]

# c = [(x%y) if x == y else 1 for x in b for y in a ]
# print(c)

# # for dictionary 
# b = {i:i*2 for i in a }
# print(b)


# num = [n for n in range(100) if 
#        sum([int(j) for j in str(n)]) % 7 == 0]
# print (num)
# under = True
# flag = "true" if under else "false"
# print(flag)


# age_limit = 18
# user_age = 17

# response = " You are not old enough" if user_age < age_limit else "You are old enough"
# print(response)