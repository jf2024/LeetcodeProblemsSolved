from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without duplicate characters.

    Time Complexity: O(N)
        - each character being visted once, amortized O(N)

    Space Complexity: O(K)
        - k = number of unique characters in the input string
    """
    counts = defaultdict(int)
    left = 0
    ans = 0

    for i in range(len(s)):
        counts[s[i]] += 1

        while counts[s[i]] > 1:
            counts[s[left]] -= 1

            if counts[s[left]] == 0:
                del counts[s[left]]
                
            left += 1

        ans = max(ans, i - left + 1)

    return ans

if __name__ == "__main__":
    print(f"Test 1: {lengthOfLongestSubstring('abcabcbb')}") # Expected: 3 ("abc")
    print(f"Test 2: {lengthOfLongestSubstring('bbbbb')}")    # Expected: 1 ("b")
    print(f"Test 3: {lengthOfLongestSubstring('pwwkew')}")   # Expected: 3 ("wke")