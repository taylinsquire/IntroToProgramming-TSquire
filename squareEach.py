def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def main():
    nums = [3, 9, 5, 2, 6, 7]

    squareEach(nums)

    print(nums)


main()