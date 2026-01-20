def repeated_character(s: str) -> str:
    """
    Given a string s, return the first character to appear twice.
    It is guaranteed that the input will have a duplicate character.

    Time and Space Complexity: O(N)
    """

    seen = set()
    for char in s:
        if char in seen:
            return char
        
        seen.add(char)



if __name__ == "__main__":
    # You can modify these test cases or add more
    test_cases = [
        "abccbaacz",
        "abcdd",
        "aabbcc",
        "xyzxyz",
    ]

    for s in test_cases:
        print(f"s={s!r} -> {repeated_character(s)}")
