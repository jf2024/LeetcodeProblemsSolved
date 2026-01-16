def getCommon(nums1: list[int], nums2: list[int]) -> int:
    # TODO: Implement logic
    pass

if __name__ == "__main__":
    # Test 1
    n1_1, n1_2 = [1, 2, 3], [2, 4]
    print(f"Test 1: {getCommon(n1_1, n1_2)}") # Expected: 2

    # Test 2
    n2_1, n2_2 = [1, 2, 3, 6], [2, 3, 4, 5]
    print(f"Test 2: {getCommon(n2_1, n2_2)}") # Expected: 2