# 01-Arrays-Strings/Prefix-Sum/LC2090_K_Radius_Subarray_Averages.py
# Problem Link: https://leetcode.com/problems/k-radius-subarray-averages/

from typing import List

def getAverages(nums: List[int], k: int) -> List[int]:
    """
    Build and return an array avgs of length n where avgs[i] is the k-radius 
    average for the subarray centered at index i.
    
    Constraints:
    - n == nums.length
    - 1 <= n <= 10^5
    - 0 <= nums[i], k <= 10^5
    """
    if k == 0:
        return nums
        
    averages = [-1] * len(nums)
    
    window_size = k + k + 1

    if k > len(nums):
        return averages
    
    curr = 0
    
    for i in range(window_size):
        curr += nums[i]
    
    averages[k] = curr // window_size

    for j in range(k+1, len(nums) - k): #when entering, curr is 37
        curr += nums[j + k] #right element we are adding
        curr -= nums[j - k - 1] #left element are deleting/subtracting
        averages[j] = curr // window_size


    return averages
            

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Standard case
    n1, k1 = [7, 4, 3, 9, 1, 8, 5, 2, 6], 3
    print(f"Test 1: {getAverages(n1, k1)}") 
    # Expected Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    # Test 2: Radius 0
    n2, k2 = [100000], 0
    print(f"Test 2: {getAverages(n2, k2)}") 
    # Expected Output: [100000]

    # Test 3: Radius larger than array
    n3, k3 = [8], 100000
    print(f"Test 3: {getAverages(n3, k3)}") 
    # Expected Output: [-1]

    # Test 4: Array length exactly window size
    n4, k4 = [1, 2, 3, 4, 5], 2
    print(f"Test 4: {getAverages(n4, k4)}")
    # Expected Output: [-1, -1, 3, -1, -1]