from collections import defaultdict
def isIsomorphic(s: str, t: str) -> bool:
    """
    Given two strings s and t, determine if they are isomorphic.
    
    Constraints:
    - 1 <= s.length <= 5 * 10^4
    - t.length == s.length
    - s and t consist of any valid ascii character.

    MY ORIGINAL IMPLEMENTATION HERE

    TIME COMPLEXITY: O(N)
        - iterate through the strings once
    SPACE COMPLEXITY; O(W)
        - where W is the size of character but since we are dealing with just the alphabet, 
        it's technicallyO(1)
    """
    mapping = defaultdict(set)
    track_set = set()

    for i in range(len(s)):
        mapping[s[i]].add(t[i]) #building the dictionary 
        track_set.add(t[i]) #keeping track of the values 

        if len(mapping[s[i]]) > 1:  #if our key has more then 1 character, return False immediatly 
            return False
    
    #if this is unbalance, that means at least two of our keys point to the same character, so return False
    #if its the same, then we know each key is pointed to a unique character (each mapping should be unique)
    # example: s = badc, t = baba
        # track_set = {b, a}, the length is 2 
        # mapping = {'b': {'b'}, 'a': {'a'}, 'd': {'b'}, 'c': {'a'}}), the length is 4 
    if len(track_set) != len(mapping): 
        return False
    
    return True


def isIsomorphic(s: str, t: str) -> bool:
    """
    Given two strings s and t, determine if they are isomorphic.
    
    Constraints:
    - 1 <= s.length <= 5 * 10^4
    - t.length == s.length
    - s and t consist of any valid ascii character.

    VERSION 2:
    The more "approiate way" I guess 
    """

    mapStoT = {}
    mapTtoS = {}

    for charS, charT in zip(s, t):
        if charS in mapStoT and mapStoT[charS] != charT:
            return False    #'e' tied to map to 'g' and then 'a'
        
        if charT in mapTtoS and mapTtoS[charT] != charS:
            return False   #'a' tied to 'b', but 'd' also wanted 'b'
        
        # when we get to this point, either both are new 
        # or they are correctly paired (reassign just to be sure)
        mapStoT[charS] = charT
        mapTtoS[charT] = charS

    return True

"""
Trace Example for Version 2 CODE 
s = "badc", t = "baba"

Starting out:
mapStoT = {}
mapTtoS = {}

Step 1: charS = 'b', charT = 'b'
    - 'b' is not in mapStoT.
    - 'b' is not in mapTtoS.
    - Action: Pair them up.
    - mapStoT = {'b': 'b'}
    - mapTtoS = {'b': 'b'}

Step 2: charS = 'a', charT = 'a'
    - 'a' is not in mapStoT.
    - 'a' is not in mapTtoS.
    - Action: Pair them up.
    - mapStoT = {'b': 'b', 'a': 'a'}
    - mapTtoS = {'b': 'b', 'a': 'a'}

Step 3: charS = 'd', charT = 'b'
    - 'd' is not in mapStoT (it thinks it's single).
    - Check mapTtoS: 'b' IS already a key.
    - Conflict: mapTtoS['b'] is 'b', but our current charS is 'd'.
    - Result: RETURN FALSE (Many-to-One violation).

Summary:
Two different characters from S ('b' and 'd') tried to map to the 
same character in T ('b').
"""

def run_tests():
    test_cases = [
        #("egg", "add", True),
        #("foo", "bar", False), #len is different false
        #("paper", "title", True), #len is same true
        ("badc", "baba", False), #len is different false
        #("a", "a", True)
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = isIsomorphic(s, t)
        passed = result == expected
        print(f"Test case {i}: s='{s}', t='{t}', expected={expected}, got={result}, passed={passed}")

if __name__ == "__main__":
    run_tests()