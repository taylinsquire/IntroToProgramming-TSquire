def sumList(nums):
    numSum = 0
    for i in range(len(nums)):
        numSum += nums[i]
    return numSum


def main():
    nums = [3, 5, 7, 9, 1, 5, 6, 4]

    numSum = sumList(nums)

    print(numSum)


main()