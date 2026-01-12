def waysToSplitArray(nums: list[int]) -> int:
    """
    Finds the number of ways to split an array into two non-empty parts
    where the sum of the left part is >= sum of the right part.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of nums.
    - Space: O(n) to store the prefix sum array.
    """
    n = len(nums)
    
    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    
    # We loop until n - 1 because the second section must have at least one number.
        # if we loop until n (len(nums)), then in the left section, our split contains every number or in other words, the last element of the prefix
        # then in our right section, there are no numbers left since the left has all of them, so its an empty array which violates the question (non-empty)
    for i in range(n - 1):
        # The sum of the first section (0 to i)
        left_section = prefix[i]
        
        # The sum of the second section (i + 1 to end)
        # Strategy: Total sum (last element of prefix) minus the left part sum
        right_section = prefix[-1] - prefix[i]
        
        if left_section >= right_section:
            ans += 1

    return ans


    """
    This Alternative method below is without needing to build that prefix array
    So instead of O(N) space complexity we can achieve O(1)

    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i] #update our running total as we go along 
            right_section = total - left_section #then subtract like normal 
            if left_section >= right_section:
                ans += 1

        return ans
    """

if __name__ == "__main__":
    n1 = [10, 4, -8, 7]
    print(f"Test 1: {waysToSplitArray(n1)}") 
    # Expected: 2 (Splits: [10 | 4, -8, 7] and [10, 4 | -8, 7])

    n2 = [2, 3, 1, 0]
    print(f"Test 2: {waysToSplitArray(n2)}") 
    # Expected: 2 (Splits: [2, 3 | 1, 0] and [2, 3, 1 | 0])