# Leetcode 1208. Get Equal Substrings Within Budget
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    """
    My Implementation

    Time Complexity: O(N) - will process each index of s and t at most twice, iterating over the characters w
    while extending the window 

    Space Complexity: O(1)
    """
    left = 0
    ans = 0
    cost = 0

    total_cost = 0

    for i in range(len(s)):
        cost = abs(ord(s[i]) - ord(t[i]))

        total_cost += cost


        while maxCost - total_cost < 0:

            total_cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        ans = max(ans, i - left + 1)
        
        
    return ans 

if __name__ == "__main__":
    # Test 1
    s1, t1, cost1 = "abcd", "bcdf", 3
    print(f"Test 1: {equalSubstring(s1, t1, cost1)}") # Expected: 3

    # Test 2
    s2, t2, cost2 = "abcd", "cdef", 3
    print(f"Test 2: {equalSubstring(s2, t2, cost2)}") # Expected: 1

    # Test 3
    s3, t3, cost3 = "abcd", "acde", 0
    print(f"Test 3: {equalSubstring(s3, t3, cost3)}") # Expected: 1