from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Check if ransomNote can be built using letters from magazine.
    Each letter in magazine can only be used once.

    This is my original solution below

    Time Complexity: O(N + M)
        - Counting the magazine = O(M)
        - checking the ransom note = O(N)

    Space Complexity: O(K)
        - K is the number of unique characters in magazine
        - if its just english letters, will be O(1) 

    """
    magazine_dict = defaultdict(int)

    #getting counts from magazine
    for letter in magazine:
        magazine_dict[letter] += 1
    
    count = 0

    #for each letter in the note, check if its in the dictionary
        #if its in the magazine_dict, add count and subtract from dict and if its 0 delete it completely
    for letter in ransomNote:
        if letter in magazine_dict:
            count += 1
            magazine_dict[letter] -= 1
            if magazine_dict[letter] == 0:
                del magazine_dict[letter]

    return True if len(ransomNote) == count else False      #if count same as len(ransomnote), its good and true


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    A more elegant solution, still uses my way of thinking but makes the 
    code cleaner 
    """

    if len(ransomNote) > len(magazine): return False

    magazine_dict = defaultdict(int)

    #getting counts from magazine
    for letter in magazine:
        magazine_dict[letter] += 1

    for letter in ransomNote:
        if magazine_dict[letter] > 0:
            magazine_dict[letter] -= 1
        else:
            return False
        
    return True

"""
One final note, you can also sort both the strings at the beginning
then check one letter at a time (think of two pointers) (is subsequence problem)
"""

if __name__ == "__main__":
    print(f"Test 1: {canConstruct('a', 'b')}")      # Expected: False
    print(f"Test 2: {canConstruct('aa', 'ab')}")     # Expected: False
    print(f"Test 3: {canConstruct('aa', 'aab')}")    # Expected: True