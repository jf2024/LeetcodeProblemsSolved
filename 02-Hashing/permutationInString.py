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


    "I SOLVED THIS PROBLEM, BUT I HAVE THE FULL SOLUTION ON LEETCODE

    ONE LAST EDGE CASE I DIDNT CONSIDER 

    ALSO, HAD TO USE GEMINI FOR SOME GUIDANCE AND HELP, IN PARTICULAR:
        - CLARFYING THE HINT ON LEETCODE THEY GAVE ABOUT FREQUENCIES
        - GEMINI SUGGESTING COMPARING TWO DICTIONARIES
        - AND THEN THINKING ABOUT FIXED WINDOW SIZES (SLIDING WINDOW PATTERN)

    ASK IT ABOUT WHAT SHOULD I HAVE BEEN THINKING AOBUT IN THIS PROBLEM? I ORIGINALLY THOUGHT ABOUT SLIDING WINDOW
    BU NEGLECTED THE FIXED SIZE VARATOIN AND ONLY FOCUSED ON DYNAMIC
    I ALSO DIDNT CONSIDER USING TWO DICTIONARIES.....
    """
    s1_dict = Counter(s1)
    s2_dict = defaultdict(int)

    for i in range(len(s1)):
        s2_dict[s2[i]] += 1

    if s1_dict == s2_dict:
        return True
    

    for i in range(len(s1), len(s2)):
        s2_dict[s2[i]] += 1 #add the incoming letter

        s2_dict[s2[i-len(s1)]] -= 1   #delete/remove the "left" letter

        if s2_dict[s2[i-len(s1)]] == 0:
            del s2_dict[s2[i-len(s1)]]

        if s1_dict == s2_dict:
            return True
    
    return False





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
