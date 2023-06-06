def calculate_grades(*args):
    gradeA = []
    gradeB = []
    gradeC = []
    gradeD = []
    gradeF = []
    dic = {}
    for list in args:
        for a in list:
            if a >= 90 and a <= 100:
                gradeA.append(a)
            if a >= 80 and a <= 89:
                gradeB.append(a)
            if a >= 70 and a <= 79:
                gradeC.append(a)
            if a >= 60 and a <= 69:
                gradeD.append(a)
            elif a < 60:
                gradeF.append(a)

    dic["A"] = len(gradeA)
    dic["B"] = len(gradeB)
    dic["C"] = len(gradeC)
    dic["D"] = len(gradeD)
    dic["F"] = len(gradeF)
    print(f"Output: {dic}")
calculate_grades([80,95,70,65,88,92,75,60,85,78,92,63,55,44,50,33,20,80])