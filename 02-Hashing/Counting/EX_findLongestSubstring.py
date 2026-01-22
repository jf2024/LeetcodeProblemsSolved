from collections import defaultdict

def find_longest_substring(s: str, k: int) -> int:
    """
    Given a string s and an integer k, find the length of the longest 
    substring that contains at most k distinct characters.
    """
    # Defaultdict basically says
    # "If I look for a key and it isn't there, don't crash. 
    # Just create the key and give it a default value of 0."
    counts = defaultdict(int)

    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1

        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0: #making sure to delete our key when it hits 0 so we can safely add the next element
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

if __name__ == "__main__":
    s1, k1 = "eceba", 2
    print(f"Test 1: {find_longest_substring(s1, k1)}") 
    # Expected: 3 ("ece")

    s2, k2 = "aa", 1
    print(f"Test 2: {find_longest_substring(s2, k2)}") 
    # Expected: 2 ("aa")

    s3, k3 = "aabacbebebe", 3
    print(f"Test 3: {find_longest_substring(s3, k3)}") 
    # Expected: 7 ("cbebebe")