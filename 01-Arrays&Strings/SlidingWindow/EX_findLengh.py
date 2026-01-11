def find_length(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subarray whose sum is less than or equal to k.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of the array. Even though there is a nested 
      while loop, each element is added once and removed at most once.
    - Space: O(1) as we only use variables for pointers and the current sum.
    """
    left = curr = ans = 0
    
    for right in range(len(nums)):
        curr += nums[right]
        
        while curr > k:
            curr -= nums[left]
            left += 1
            
        ans = max(ans, right - left + 1)
    
    return ans

if __name__ == "__main__":
    # Test 1: Standard case
    nums1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    k1 = 8
    print(f"Test 1 (k={k1}): {find_length(nums1, k1)}")  # Expected: 4 (Subarray [4, 2, 1, 1])

    # Test 2: k is very small
    nums2 = [1, 2, 3]
    k2 = 0
    print(f"Test 2 (k={k2}): {find_length(nums2, k2)}")  # Expected: 0

    # Test 3: All elements satisfy k
    nums3 = [1, 1, 1]
    k3 = 5
    print(f"Test 3 (k={k3}): {find_length(nums3, k3)}")  # Expected: 3