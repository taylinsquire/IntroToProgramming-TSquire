import math

n = int(input("Enter the amount of terms you want to sum to approximate pi: "))
piSum = 0


for i in range (1, n+1):
    piSum = piSum + (4/((2 * i) - 1)) * ((-1)**(i+1))

piError = abs(math.pi - piSum)

print("The error using", n, "terms is:", piError)
print("The actual value for pi is:", math.pi)
print("Our approximated value for pi is:", piSum)
