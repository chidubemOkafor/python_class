# def find_common_elements(*args):
#     common_element = []
#     for ar in args[0]:
#         if ar in list(set(args[0]) & set(args[1])):
#             common_element.append(ar)

#     return common_element

# result = find_common_elements(["name","age","class","john","mary"],["name","age","john"])
# print(result)

# common_elements = []

# def find_common_elements1(*args):
 
#     print(args[0])
#     print(args[1])
#     if args[0] == args[1]:
#         common_elements.append(args[0])
#         print(args)
 
# find_common_elements1(["name","age","class","john","mary"],["name","age","john"])
# print(common_elements)

ran1 = [1,2,3,4,5]
ran2 = [2,5,3,6,7]

def find_common_elements(ran1, ran2):
    ran3 = []
    for i in ran1:
        for j in ran2:
            if i == j:
                ran3.append(i)
    return ran3

result = find_common_elements(ran1, ran2)  

print(result)