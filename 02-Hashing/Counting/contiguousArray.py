from collections import defaultdict

def findMaxLength(self, nums: list[int]) -> int:
    first_seen = defaultdict(int)
    first_seen[0] = -1      #base case, sum 0 (key) is at index -1 

    curr = 0
    ans = 0

    for i in range(len(nums)):
        # increase curr by 1 if 1, decrease it by -1 if 0 
        if nums[i] == 0:
            curr -= 1
        else:
            curr += 1

        # if we have seen the curr before, then theres an equal balance
        if curr in first_seen:
            ans = max(ans, i - first_seen[curr])    #current index minus the first time we saw that sum 
        else:
            first_seen[curr] = i    #if curr not in dict, store it

    return ans

"""
    CONCEPTUAL NOTES:
    1) THE TRANSFORMATION: We treat '1' as +1 and '0' as -1. This turns 
       the problem into finding a subarray with a sum of 0.
        - key detail is "equal" number of things which the problem asks, which means the 
        difference is zero and if we treat 0 as a -1, then our "equal balance" problem turns into
        a search for a sum of 0
       
    2) EQUAL BALANCE: If the running sum (prefix sum) is the same at 
       two different indices, the net change between those points was 0.
       This means the number of +1s and -1s was exactly equal.
        - its a prefix sum because it mentions contiguous subarray and looking for an 
        exact target
       
    3) WHY START AT -1? We initialize {0: -1} because a sum of 0 
       exists "before" the array starts. This allows us to find 
       valid subarrays that start at index 0.
       
    4) WHY NO UPDATE? We only store the FIRST time we see a sum.
       To maximize length, we want the earliest possible start and 
       the latest possible end.
       
    Time Complexity: O(N) - We iterate through the array once.
    Space Complexity: O(N) - Hash map can store up to N prefix sums.

    This is a prefix sum problem:
        - need to find a contiguous subarray
        - looking for an exact target (equal counts)
    """


if __name__ == "__main__":
    c1 = [0, 1]
    print(f"Test 1: {findMaxLength(c1)}") 
    # Expected: 2

    c2 = [0, 1, 0]
    print(f"Test 2: {findMaxLength(c2)}") 
    # Expected: 2

    c3 = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    print(f"Test 3: {findMaxLength(c3)}") 
    # Expected: 6