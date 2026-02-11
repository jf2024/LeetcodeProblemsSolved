from collections import defaultdict

def maximum_erasure_value(nums: list[int]) -> int:
    """
    You are given an array of positive integers nums and want to erase a 
    subarray containing unique elements. The score you get by erasing the 
    subarray is equal to the sum of its elements.
    
    Return the maximum score you can get by erasing exactly one subarray.

    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^4

    Time Complexity: O(N)
    Space Complexity: O(N)

    VERSION 1 - MY ORIGINAL IMPLEMENTATION
    """
    dic = defaultdict(int)
    ans = 0
    left = 0
    curr = 0

    for i in range(len(nums)):
        dic[nums[i]] += 1           #key is number, value is number of times it appears
        curr += nums[i]             #add to curr

        while dic[nums[i]] > 1: 
            curr -= nums[left]      #subtract curr amount to the number 
            dic[nums[left]] -= 1    #decrease occurance of that number once 
            left += 1               #shift the left side by one

        ans = max(ans, curr)        #ensure we get the max sum of our subarray 

    return ans


def maximumUniqueSubarray(nums: list[int]) -> int:
    """
    VERSION 2

    INSTEAD OF A HASHMAP/DICTOINARY, WE CAN ALSO USE A SET TO SOLVE IT

    SAME TIME AND SPACE COMPLEXITY
    """
    counts = set()
    ans = 0
    curr = 0
    left = 0

    for num in range(len(nums)):
        curr += nums[num]

        while nums[num] in counts:
            curr -= nums[left]
            counts.remove(nums[left])
            left += 1

        counts.add(nums[num])
        ans = max(ans, curr)

    return ans


def run_tests():
    test_cases = [
        # (nums, expected)
        # ([4, 2, 4, 5, 6], 17), # Optimal subarray is [2, 4, 5, 6]
        # ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8), # Optimal subarray is [5, 2, 1] or [1, 2, 5]
        # ([1, 1, 1, 1, 1], 1),
        # ([1, 2, 3, 4, 5], 15),
        # ([10, 20, 30, 10, 40], 100), # [20, 30, 10, 40]
        ([10000,1,10000,1,1,1,1,1,1], 10001)
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = maximum_erasure_value(nums)
        passed = result == expected
        print(f"Test case {i}: nums={nums}, expected={expected}, got={result}, passed={passed}")


if __name__ == "__main__":
    run_tests()
