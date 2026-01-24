from collections import defaultdict

def subarraySum(nums: list[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the total 
    number of subarrays whose sum equals to k.

    Time Complexity: O(N) because we iterate the array once
    Space Complexity: O(N) because in worst case (array is all positve numbers), every prefix sum would be unique and stored in the hash map
    """
    counts = defaultdict(int)
    counts[0] = 1 #base case: prefix sum of 0 exists before we start (our empty subarray)
    curr = ans = 0

    for num in nums:
        curr += num     #updaing our prefix sum 
        ans += counts[curr - k] #check if curr - k exists in our dictionary, if so add and if not, would just be 0 

        counts[curr] += 1 #then add that current prefix sum to the dictionary 

    return ans


"""
1) so our curr is basically our prefix sum 
2) we subtract our current prefix sum with k and see if that value is in the dictionary
3) if it is in the dictionary, we would add counts[curr - k] to our answer because it represents
the number of times we have seen that specific prefix sum (the curr - k) in the past and stored in the dictionary
4) if its not, it would just be 0 and wont add anything to our current answer


and then we would add the current prefix sum to our dictionary and move on  
"""

if __name__ == "__main__":
    n1, k1 = [1, 1, 1], 2
    print(f"Test 1: {subarraySum(n1, k1)}") 
    # Expected: 2 (The first two 1s, and the last two 1s)

    n2, k2 = [1, 2, 3], 3
    print(f"Test 2: {subarraySum(n2, k2)}") 
    # Expected: 2 ([1, 2] and [3])

    n3, k3 = [1, -1, 1, 1, 1], 2
    print(f"Test 3: {subarraySum(n3, k3)}")
    # Expected: 4