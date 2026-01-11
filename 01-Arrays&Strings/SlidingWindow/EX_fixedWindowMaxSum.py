def find_max_sum(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of a subarray with a fixed length k.
    
    Complexity Analysis:
    - Time: O(n)
    - Space: O(1)
    
    """
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    
    for i in range(k, len(nums)):
        curr += nums[i]
        curr -= nums[i - k]
        
        ans = max(ans, curr)
        
    return ans

if __name__ == "__main__":
    n1, k1 = [3, -1, 4, 12, -8, 5, 6], 4
    print(f"Max sum of window {k1}: {find_max_sum(n1, k1)}") #should be 18