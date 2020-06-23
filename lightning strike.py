sos = 1100

timeElapsed = float(input("Enter the time elapsed between the flash and the thunder in seconds: "))

distance = (timeElapsed * sos)/5280

print("The lightning is", distance, "miles away")