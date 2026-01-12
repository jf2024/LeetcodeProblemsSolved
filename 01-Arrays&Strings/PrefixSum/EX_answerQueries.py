def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    """
    Determines if the sum of subarrays defined by queries is less than a limit.
    
    Complexity Analysis:
    - Time: O(n + m) where n is the length of nums and m is the number of queries.
      Building the prefix sum takes O(n), and answering each query takes O(1).
    - Space: O(n) to store the prefix sum array.
    
    """
    # Step 1: Build the Prefix Sum array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1]) #prefix[-1] same as prefix[i-1]
    
    ans = []
    
    # Step 2: Process each query [x, y]
    for x, y in queries:
        # Use the formula: prefix[j] - prefix[i] + nums[i]
        # In this case, x is i and y is j.
        curr_sum = prefix[y] - prefix[x] + nums[x]
        
        # Check against limit and append result
        ans.append(curr_sum < limit)
        
    return ans

# --- Test Cases ---
if __name__ == "__main__":
    nums_1 = [1, 6, 3, 2, 7, 2]
    queries_1 = [[0, 3], [2, 5], [2, 4]]
    limit_1 = 13
    
    result = answer_queries(nums_1, queries_1, limit_1)
    print(f"Test 1 Results: {result}") 
    # Expected: [True, False, True] (Sums: 12, 14, 12)