def checkIfPangram(sentence: str) -> bool:
    pass

if __name__ == "__main__":
    # Test 1
    s1 = "thequickbrownfoxjumpsoverthelazydog"
    print(f"Test 1: {checkIfPangram(s1)}") # Expected: True

    # Test 2
    s2 = "leetcode"
    print(f"Test 2: {checkIfPangram(s2)}") # Expected: False