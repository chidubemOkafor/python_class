score1 = float(input("mathematics: ",))
score2 = float(input("english: ",))
score3 = float(input("chemistry: ",))
score4 = float(input("physics: ",))
print("============")
def grade_average(*args):
    for i in args:
       length = len(i)
       totalGrade = sum(i)
       av = round(totalGrade / length)
    if av >= 90 and av <= 100:
        print(f"👍 A: {av}")
        print("============")
    elif av >= 80 and av <= 89:
        print(f"🌝 B: {av}")
        print("============")
    elif av >= 70 and av <= 79:
        print(f"🚶 C: {av}") 
        print("============")
    elif av >= 60 and av <= 69:
        print(f"🤒 D: {av}")    
        print("============")
    else:
        print(f"😿 F: {av}") 
        print("============")
        
grade_average([score1,score2,score3,score4])