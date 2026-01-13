# 1480. Running Sum of 1d Array
# Problem Link: https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums: list[int]) -> list[int]:
    """
    Given an array nums, return the running sum of nums.
    The running sum is defined as: runningSum[i] = sum(nums[0]…nums[i]).
    
    Complexity Analysis (Target):
    - Time: O(n) where n is the length of nums.
    - Space: O(1) if we modify the input array, or O(n) if we create a new one.
    
    """
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1]) #can also do prefix[i-1]

    return prefix


if __name__ == "__main__":
    # Test 1
    n1 = [1, 2, 3, 4]
    print(f"Test 1: {runningSum(n1)}") 
    # Expected Output: [1, 3, 6, 10]

    # Test 2
    n2 = [1, 1, 1, 1, 1]
    print(f"Test 2: {runningSum(n2)}") 
    # Expected Output: [1, 2, 3, 4, 5]

    # Test 3
    n3 = [3, 1, 2, 10, 1]
    print(f"Test 3: {runningSum(n3)}") 
    # Expected Output: [3, 4, 6, 16, 17]