days = int(input("Enter the number of days the student has been in their course: "))
assignments = int(input("Enter the number of assignments the student has completed: "))

progress = (assignments / days) * 100

print("This students progress is at " + str(progress) + "%")
