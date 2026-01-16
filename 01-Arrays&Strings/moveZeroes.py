def moveZeroes(nums: list[int]) -> None:
    # TODO: Implement logic (Modify nums in-place)
    pass

if __name__ == "__main__":
    # Test 1
    n1 = [0, 1, 0, 3, 12]
    moveZeroes(n1)
    print(f"Test 1: {n1}") # Expected: [1, 3, 12, 0, 0]

    # Test 2
    n2 = [0]
    moveZeroes(n2)
    print(f"Test 2: {n2}") # Expected: [0]