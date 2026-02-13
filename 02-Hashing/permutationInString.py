from collections import Counter
from collections import defaultdict

def check_inclusion(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
    or false otherwise.
    
    A permutation means that one of s1's permutations is a contiguous substring 
    of s2.
    
    Constraints:
    - 1 <= s1.length, s2.length <= 10^4
    - s1 and s2 consist of lowercase English letters.

    Time Complexity: O(N)
    Space Complexity: O(1) - since we are just dealing with characters


    Note: I didn't solve this fully on my own, I had to ask gemini for some hints and guidance, specifically:
        - it mentioned two dictionaries 
        - as well as fixed size window (sliding window variation)

    And then I solved it on my own 
    """
    s1_dict = Counter(s1)
    s2_dict = defaultdict(int)

    #if s1 is bigger, then return false cause its impossible 
    if len(s1) > len(s2):
        return False

    #building our first window 
    for i in range(len(s1)):
        s2_dict[s2[i]] += 1

    #check if that first window is equal, if so return and if not continue to the second loop
    if s1_dict == s2_dict:
        return True
    

    for i in range(len(s1), len(s2)):
        s2_dict[s2[i]] += 1 #add the incoming letter (from the right)
        s2_dict[s2[i-len(s1)]] -= 1  #delete/remove the "left" letter

        if s2_dict[s2[i-len(s1)]] == 0: 
            del s2_dict[s2[i-len(s1)]]

        #doing our check
        if s1_dict == s2_dict:
            return True
    
    return False   #if we made it this far, couldnt find it so its false


"""
Additional Notes to consider: 
1) How to Recongize this was a fixed sliding window problem:
    - the problem involves continuous range (subarray string)
    - the problem gives us a SPECIFIC length
        - to explain further, a permutation of s1 must be the same length as s1.
        - ex: if s1 is 3 characters long, we are looking for a "window" that is 3 characters long
"""


def run_tests():
    test_cases = [
        # (s1, s2, expected)
        ("ab", "eidbaooo", True),  # s2 contains "ba"
        ("ab", "eidboaoo", False), # s2 does not contain a permutation
        ("adc", "dcda", True),     # s2 contains "dca"
        ("hello", "ooolleoooeh" , False),
        ("abc", "bbbca", True),    # s2 contains "bca"
    ]

    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        result = check_inclusion(s1, s2)
        passed = result == expected
        print(f"Test case {i}: s1={s1!r}, s2={s2!r}, expected={expected}, got={result}, passed={passed}")


if __name__ == "__main__":
    run_tests()
