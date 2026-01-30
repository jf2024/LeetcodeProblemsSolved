from collections import defaultdict

def sumOfUnique(nums: list[int]) -> int:
    """
    Given an integer array nums, return the sum of all elements 
    that appear exactly once in the array.

    My original implementation here:

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    dic = defaultdict(int)

    for num in nums:
        dic[num] += 1

    total = 0
    for key, value in dic.items():
        if value == 1:
            total += key

    return total 

#we do two passes here, one for the original input and then the dictionary 

#there is a one pass solution though



if __name__ == "__main__":
    n1 = [1, 2, 3, 2]
    print(f"Test 1: {sumOfUnique(n1)}") # Expected: 4

    n2 = [1, 1, 1, 1, 1]
    print(f"Test 2: {sumOfUnique(n2)}") # Expected: 0

    n3 = [1, 2, 3, 4, 5]
    print(f"Test 3: {sumOfUnique(n3)}") # Expected: 15