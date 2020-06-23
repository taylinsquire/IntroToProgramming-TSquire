def happy():
    print("Happy birthday to you!")


def sing(name):
    happy()
    happy()
    print("Happy birthday, dear " + name + ".")
    happy()


def main():
    sing("Fred")
    print()
    sing("Lucy")


main()
