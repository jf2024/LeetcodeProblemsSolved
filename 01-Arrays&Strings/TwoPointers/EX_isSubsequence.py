def is_subsequence(s: str, t: str) -> bool:
    """
    Determines if string 's' is a subsequence of string 't'.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of the target string 't'. 
      We scan 't' at most once.
    - Space: O(1) as we only use two integer pointers.
    """
    i = j = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s) #if i matches length of s, then its a subsequence, else its false

if __name__ == "__main__":
    # Test 1: Is a subsequence
    s1, t1 = "ace", "abcde"
    print(f"Test 1 ('{s1}' in '{t1}'): {is_subsequence(s1, t1)}") # Expected: True

    # Test 2: Not a subsequence (Wrong order)
    s2, t2 = "aec", "abcde"
    print(f"Test 2 ('{s2}' in '{t2}'): {is_subsequence(s2, t2)}") # Expected: False

    # Test 3: Empty string s (Always a subsequence)
    s3, t3 = "", "ahbgdc"
    print(f"Test 3 ('{s3}' in '{t3}'): {is_subsequence(s3, t3)}") # Expected: True