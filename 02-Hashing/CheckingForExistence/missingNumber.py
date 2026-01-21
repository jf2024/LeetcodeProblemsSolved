def missingNumber(nums: list[int]) -> int:
    """
    Time and Space Complexity: O(N)
    """

    """
    My oriignal solution below
    """
    # set_nums = set(nums)

    # if len(nums) not in set_nums:
    #     return len(nums)

    # for i in range(len(nums)):
    #     if i not in set_nums:
    #         return i
        
    # return -1


    """
    Getting rid of the if statement
    """
    set_nums = set(nums)

    for i in range(len(nums) + 1):
        if i not in set_nums:
            return i
        
    return -1


# note, can have O(1) space complexity by doing the gauss summation formula
# i didnt show it cause it doesnt rlly use sets or hashmaps, can ask chat or gemini to see what it looks like

if __name__ == "__main__":
    n1 = [3, 0, 1]
    print(f"Test 1: {missingNumber(n1)}") # Expected: 2

    n2 = [0, 1]
    print(f"Test 2: {missingNumber(n2)}") # Expected: 2

    n3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Test 3: {missingNumber(n3)}") # Expected: 8