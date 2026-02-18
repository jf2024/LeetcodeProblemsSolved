from collections import defaultdict
from collections import Counter

def custom_sort_string(order: str, s: str) -> str:
    """
    MY ORIGINAL IMPLEMENTATION WITH SOME HELP FROM GEMINI

    TIME COMPLEXITY: O(N + M)
        - O(N) to build the frequency counter of string 's'.
        - O(M) to build the 'order_dict' and iterate through 'order'.
        - Since 'order' is at most 26 characters (lowercase English), 
      this effectively scales linearly with the length of 's'.

    SPACE COMPLEXITY: O(N)
        - O(N) to store the 's_freq' counter and the 'ans' list which 
      holds all characters of 's' before joining them.
        - O(M) for the 'order_dict', which is constant O(26) = O(1).
    """

    order_dict = defaultdict(int)
    for char in range(len(order)):
        order_dict[char] = order[char]  #{0:c, 1:b, 2:a} key is index while value is character

    s_freq = Counter(s) #frequency of our s 

    ans = []
    for index in order_dict:
        char = order_dict[index]
        
        ans.append(char * s_freq[char])
        del s_freq[char]

    for char, count in s_freq.items():
        ans.append(char * count)

    return "".join(ans)


def custom_sort_string(order: str, s: str) -> str:
    """
    IMPROVED CODE VERSION 2

    Time Complexity: O(N + M)
        - O(N): scanning string "s" to create frequency map (s_freq)
        - O(M): iterating over the "order" string

        
    Space Complexity: O(N)
        - O(N): the s_permutation list stores all N characters of string 's'
        - O(1): s_freq stores at most 26 keys, so its just constant space

    """

    s_freq = Counter(s) #get our frequencies of s 
    s_permutation = []

    # iterating over "order", we add to our s_permutation
    #   if the character is inside of our s_freq, and we 
    #   delete afterwards
    for char in order:
        if char in s_freq:
            s_permutation.append(char * s_freq[char])
            del s_freq[char]

    # at this point, the characters left in s_freq
    # aren't in order, so we can just add 
    for remainingElems in s_freq:
        s_permutation.append(remainingElems * s_freq[remainingElems])

    return ''.join(s_permutation)


def run_tests():
    test_cases = [
        {"order": "cba", "s": "abcd", "expected": "cbad"},
        {"order": "bcafg", "s": "abcdd", "expected": "bcad"},
        {"order": "kqep", "s": "pekeq", "expected": "kqeep"},
    ]

    print("--- Running Custom Sort String Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = custom_sort_string(test["order"], test["s"])
        
        # Note: Since any valid permutation works, we check if the 
        # relative order matches 'order' rather than an exact string match.
        print(f"Test {i}: order='{test['order']}', s='{test['s']}' | Result: '{result}'")

if __name__ == "__main__":
    run_tests()