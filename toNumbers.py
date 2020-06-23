def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])


def main():
    strList = ["4", "6", "20198", "5001", "999"]

    toNumbers(strList)

    for i in range(len(strList)):
        print(strList[i], type(strList[i]))


main()