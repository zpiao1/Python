__author__ = 'zpiao1'
print("note: enter -1 to end.")
score = int(input("input score: "))
if score == -1:
    print("max_score =  0\nmin_score =  0")
else:
    max_score = min_score = score
    while True:
        if 0 <= score < 45:
            print("  grade: F")
        elif score < 65:
            print("  grade: C")
        elif score < 85:
            print("  grade: B")
        elif score < 100:
            print("  grade: A")
        score = int(input("input score: "))
        if score == -1:
            print("max_score = ", max_score)
            print("min_score = ", min_score)
            break
        elif score > max_score:
            max_score = score
        elif score < min_score:
            min_score = score