def equalSubstring(s: str, t: str, maxCost: int) -> int:
    # TODO: Implement logic
    pass

if __name__ == "__main__":
    # Test 1
    s1, t1, cost1 = "abcd", "bcdf", 3
    print(f"Test 1: {equalSubstring(s1, t1, cost1)}") # Expected: 3

    # Test 2
    s2, t2, cost2 = "abcd", "cdef", 3
    print(f"Test 2: {equalSubstring(s2, t2, cost2)}") # Expected: 1

    # Test 3
    s3, t3, cost3 = "abcd", "acde", 0
    print(f"Test 3: {equalSubstring(s3, t3, cost3)}") # Expected: 1