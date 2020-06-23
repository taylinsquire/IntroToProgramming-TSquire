def main():
    print("Table")
    print("---------------------")
    print("C: 0 | F: 32")

    for i in range(100):
        if (i + 1) % 10 == 0:
            tableFahrenheit = 9/5 * (i + 1) + 32
            print("C:", i + 1, "| F:", tableFahrenheit)


    for j in range(5):
        print()

        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
