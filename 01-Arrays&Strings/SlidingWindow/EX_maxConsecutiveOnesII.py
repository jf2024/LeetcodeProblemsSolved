def find_length(s: str) -> int:
    """
    Finds the length of the longest substring of 1s achievable by flipping at most one 0.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of string s. Each character is visited by 
      the left and right pointers at most once.
    - Space: O(1) as we only store a few integer variables.

    In other words, what is the longest substring that contains at most one "0" 
    """

    left = curr = ans = 0
    
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        
        # While we have more than one 0, the window is invalid.
        # Shrink from the left until we have only one 0 again.
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        
        # Update the maximum length found so far
        ans = max(ans, right - left + 1)
    
    return ans

if __name__ == "__main__":
    # Test 1: Example from prompt
    s1 = "1101100111"
    print(f"Test 1 ('{s1}'): {find_length(s1)}") # Expected: 5

    # Test 2: No zeros in string
    s2 = "1111"
    print(f"Test 2 ('{s2}'): {find_length(s2)}") # Expected: 4

    # Test 3: Multiple zeros
    s3 = "0001"
    print(f"Test 3 ('{s3}'): {find_length(s3)}") # Expected: 2 (flip one 0 to get "01" or "10")