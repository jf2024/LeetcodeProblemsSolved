def reversePrefix(word: str, ch: str) -> str:
    # TODO: Implement logic
    pass

if __name__ == "__main__":
    # Test 1
    w1, c1 = "abcdefd", "d"
    print(f"Test 1: {reversePrefix(w1, c1)}") # Expected: "dcbaefd"

    # Test 2
    w2, c2 = "xyxzxe", "z"
    print(f"Test 2: {reversePrefix(w2, c2)}") # Expected: "zxyxxe"

    # Test 3
    w3, c3 = "abcd", "z"
    print(f"Test 3: {reversePrefix(w3, c3)}") # Expected: "abcd"