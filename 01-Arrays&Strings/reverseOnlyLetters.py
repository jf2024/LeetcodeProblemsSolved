def reverseOnlyLetters(s: str) -> str:
    # TODO: Implement logic
    pass

if __name__ == "__main__":
    # Test 1
    s1 = "ab-cd"
    print(f"Test 1: {reverseOnlyLetters(s1)}") # Expected: "dc-ba"

    # Test 2
    s2 = "a-bC-dEf-ghIj"
    print(f"Test 2: {reverseOnlyLetters(s2)}") # Expected: "j-Ih-gfE-dCba"

    # Test 3
    s3 = "Test1ng-Leet=code-Q!"
    print(f"Test 3: {reverseOnlyLetters(s3)}") # Expected: "Qedo1ct-eeL=tseT-n!"