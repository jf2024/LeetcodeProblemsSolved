def maxVowels(s: str, k: int) -> int:
    """
    Given a string s and an integer k, return the maximum number of vowel letters
    in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    My original solution
    Works and passes all test cases but my time complexity would be O(N x K) because we are maintaing a physical list
    of characters in the window
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    string_list = []
    tracker = 0
    ans = 0

    for c in range(k):
        if s[c] in vowels:
            tracker += 1
        string_list.append(s[c])

    ans = max(ans, tracker)

    for c in range(k, len(s)):
        if s[c] in vowels:
            tracker += 1

        if s[c - k] in vowels:
            tracker -= 1

        string_list.append(s[c]) #adding the right
        string_list.remove(s[c - k])    #removing the left

        ans = max(ans, tracker)

    return ans

def maxVowels(s: str, k: int) -> int:
    """
    Given a string s and an integer k, return the maximum number of vowel letters
    in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    MUCH BETTER SOLUTION HERE
    O(N)
    The intended way! Don't need to build the list of characters
    """
    
    vowels_set = ['a', 'e', 'i', 'o', 'u']

    count = 0
    ans = 0

    for c in range(k):
        if c in vowels_set:
            count += 1

    ans = count

    for c in range(k, len(s)):
        if c in vowels_set:
            count += 1

        if s[c - k] in vowels_set:
            count -= 1

        ans = max(ans, count)
        
    return ans


if __name__ == "__main__":
    s1, k1 = "abciiidef", 3
    print(f"Test 1: {maxVowels(s1, k1)}") # Expected: 3

    s2, k2 = "aeiou", 2
    print(f"Test 2: {maxVowels(s2, k2)}") # Expected: 2

    s3, k3 = "leetcode", 3
    print(f"Test 3: {maxVowels(s3, k3)}") # Expected: 2