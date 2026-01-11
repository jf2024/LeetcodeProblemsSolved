def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    """
    Returns the number of contiguous subarrays where the product of elements is < k.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of nums.
    - Space: O(1) as we use a fixed amount of extra space.
    
    Pattern: Dynamic Sliding Window (Counting Subarrays).
    Logic:
    - The number of valid subarrays ending at 'right' is equal to the 
      window size: (right - left + 1).
    """
    # Edge case: if k is 0 or 1, and nums has positive integers, 
    # no product can be strictly less than k.
    if k <= 1:
        return 0

    ans = left = 0
    curr = 1 

    for right in range(len(nums)):
        curr *= nums[right]
        
        while curr >= k:
            curr //= nums[left]
            left += 1
            
        # Key Formula: The window size represents the count of new 
        # valid subarrays that end at the current 'right' index.
        ans += (right - left + 1)

    return ans

if __name__ == "__main__":
    # Test 1: Example from prompt
    n1, k1 = [10, 5, 2, 6], 100
    print(f"Test 1: {numSubarrayProductLessThanK(n1, k1)}") # Expected: 8

    # Test 2: Edge case k=0
    n2, k2 = [1, 2, 3], 0
    print(f"Test 2: {numSubarrayProductLessThanK(n2, k2)}") # Expected: 0

    # Test 3: Single element array
    n3, k3 = [10], 100
    print(f"Test 3: {numSubarrayProductLessThanK(n3, k3)}") # Expected: 1