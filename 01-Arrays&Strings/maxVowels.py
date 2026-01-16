def maxVowels(s: str, k: int) -> int:
    # TODO: Implement logic
    pass

if __name__ == "__main__":
    # Test 1
    s1, k1 = "abciiidef", 3
    print(f"Test 1: {maxVowels(s1, k1)}") # Expected: 3

    # Test 2
    s2, k2 = "aeiou", 2
    print(f"Test 2: {maxVowels(s2, k2)}") # Expected: 2

    # Test 3
    s3, k3 = "leetcode", 3
    print(f"Test 3: {maxVowels(s3, k3)}") # Expected: 2