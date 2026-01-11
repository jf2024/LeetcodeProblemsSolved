def check_if_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome using the Two Pointers technique.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of the string. We visit each character at most once.
    - Space: O(1) as we only use two integer variables (left and right).
    
    Pattern: Converging Pointers (Start at edges, move toward center).
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Standard Palindrome
    test1 = "racecar"
    print(f"Test 1 ('{test1}'): {check_if_palindrome(test1)}") # Expected: True

    # Test 2: Not a Palindrome
    test2 = "leetcode"
    print(f"Test 2 ('{test2}'): {check_if_palindrome(test2)}") # Expected: False

    # Test 3: Symmetry
    test3 = "abcdcba"
    print(f"Test 3 ('{test3}'): {check_if_palindrome(test3)}") # Expected: True