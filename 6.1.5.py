def gr(ball):

    if ball >= 4.0:
        grade = "A"
    elif ball >= 3.0:
        grade = "B"
    elif ball >= 2.0:
        grade = "C"
    elif ball >= 1.0:
        grade= "D"
    elif ball >= 0.0:
        grade = "F"
    else:
        grade = 'некор. балл'
    return grade

bal = float(input())
print(gr(bal))
