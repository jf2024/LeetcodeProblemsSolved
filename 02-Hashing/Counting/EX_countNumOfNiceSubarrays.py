from collections import defaultdict

def numberOfSubarrays(nums: list[int], k: int) -> int:
    """
    Given an array of integers nums and an integer k, return the 
    number of "nice" subarrays (subarrays with exactly k odd numbers).
    """
    counts = defaultdict(int)
    counts[0] = 1 #base case with empty subarray 
    ans = curr = 0

    for num in nums:
        curr += num % 2     #wil either add 1 if num is odd or 0 if even
        ans += counts[curr - k]     #check history
        counts[curr] += 1   #update frequency of the odd count 

    return ans

if __name__ == "__main__":
    n1, k1 = [1, 1, 2, 1, 1], 3
    print(f"Test 1: {numberOfSubarrays(n1, k1)}") 
    # Expected: 2 ([1,1,2,1] and [1,2,1,1])

    n2, k2 = [2, 4, 6], 1
    print(f"Test 2: {numberOfSubarrays(n2, k2)}") 
    # Expected: 0

    n3, k3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2
    print(f"Test 3: {numberOfSubarrays(n3, k3)}") 
    # Expected: 16