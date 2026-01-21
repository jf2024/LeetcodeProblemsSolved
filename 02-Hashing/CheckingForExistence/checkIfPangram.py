def checkIfPangram(sentence: str) -> bool:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    For my Original Solution below
    """
    char_list = set()

    for i in sentence:
        char_list.add(i)

    return len(char_list) == 26

def checkIfPangram(sentence: str) -> bool:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """

    #can convert str to a set
    seen = set(sentence)

    return len(seen) == 26

if __name__ == "__main__":
    # Test 1
    s1 = "thequickbrownfoxjumpsoverthelazydog"
    print(f"Test 1: {checkIfPangram(s1)}") # Expected: True

    # Test 2
    s2 = "leetcode"
    print(f"Test 2: {checkIfPangram(s2)}") # Expected: False