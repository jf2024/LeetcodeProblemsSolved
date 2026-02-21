# def make_good(s: str) -> str:
#     """
#     Given a string s of lower and upper case English letters, returns a 
#     'good' version of the string.
    
#     A string is 'good' if it doesn't have two adjacent characters s[i] 
#     and s[i+1] where s[i] and s[i+1] are the same letter but different cases.
    
#     Example:
#     - "leEeetcode" -> "leetcode"
#     - "abBAcC"     -> ""
#     - "s"          -> "s"
    
#     Constraints:
#     - 1 <= s.length <= 100
#     - s contains only lower and upper case English letters.

#     MY ORIGINAL IMPLEMENTATION 

#     REALLY JANK BUT IT WORKS
#     """
#     stack = []

#     for char in s: 
#         if stack and stack[-1].islower() and char.isupper() and stack[-1].lower() == char.lower(): #checks eE case
#             stack.pop()
#         elif stack and stack[-1].isupper() and char.islower() and stack[-1].lower() == char.lower():    #checks Ee case
#             stack.pop()
#         else:
#             stack.append(char)

#     return "".join(stack)

def make_good(s: str) -> str:
    """
    "CLEANER" SOLUTION VERSION 2

    Basically just putting it into one if condition 

    """
    stack = []

    for char in s: 
        if stack and stack[-1].lower() == char.lower() and (
            (stack[-1].islower() and char.isupper()) or 
            (stack[-1].isupper() and char.islower())):

            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

def make_good(s: str) -> str:
    """
    VERSION 3

    The cleanest way actually is using the "ord" function 

    the lowercase and uppercase version of each letter is 32 decimals away 
    ex: ord('a') is 97 and ord('A') is 65
        - 97 - 65 = 32 

    So if we just subtract the ord of both characters, take the absolute value and if its 
    32, then we know to pop and move on. If its not 32, then just add like normal

    """
    stack = []

    for curr_char in s:
        if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(curr_char)
    
    return "".join(stack)


"""
TIME IS O(N)

SPACE IS O(N)

FOR ALL 3 VERSIONS
"""

def run_tests():
    test_cases = [
        ("leEeetcode", "leetcode"),
        ("abBAcC", ""),
        ("s", "s"),
        ("Pp", ""),
        ("kkKk", "kk")
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = make_good(s)
        passed = result == expected
        print(f"Test case {i}: s={s!r}, expected={expected!r}, got={result!r}, passed={passed}")


if __name__ == "__main__":
    run_tests()
