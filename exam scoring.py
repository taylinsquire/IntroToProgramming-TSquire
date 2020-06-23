score = float(input("Enter an exam score out of 100: "))


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 70:
    grade = "D"
else:
    grade = "F"

print("A score of", score, "is an", grade)
