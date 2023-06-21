def add(x,y):
    return x + y

def sub(a,y):
    return a - y

ran1 = [1,2,3,4,5]
ran2 = [2,5,3,6,7]

def find_common_elements(ran1, ran2):
    ran3 = []
    for i in ran1:
        for j in ran2:
            if i == j:
                ran3.append(i)
    return ran3

