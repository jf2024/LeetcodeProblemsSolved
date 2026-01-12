# 1413. Minimum Value to Get Positive Step by Step Sum
# Problem Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

def minStartValue(nums: list[int]) -> int:
    """
    Given an array of integers nums, you start with an initial positive value startValue.
    Return the minimum positive value of startValue such that the step by step sum 
    is never less than 1.
    
    Complexity Analysis (Target):
    - Time: O(n) where n is the length of nums.
    - Space: O(1) if we track the running sum in a variable.
    """
    # ---------------------------------------------------------
    # TODO: YOUR LOGIC HERE
    # ---------------------------------------------------------
    pass

if __name__ == "__main__":
    # Test 1
    n1 = [-3, 2, -3, 4, 2]
    print(f"Test 1: {minStartValue(n1)}") 
    # Expected Output: 5

    # Test 2
    n2 = [1, 2]
    print(f"Test 2: {minStartValue(n2)}") 
    # Expected Output: 1

    # Test 3
    n3 = [1, -2, -3]
    print(f"Test 3: {minStartValue(n3)}") 
    # Expected Output: 5