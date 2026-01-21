def countElements(arr: list[int]) -> int:
    """
    Time and Space Complexity: O(N)
    """
    set_nums = set(arr)
    count = 0

    for num in arr:
        if num + 1 in set_nums:
            count += 1
    return count

if __name__ == "__main__":
    a1 = [1, 2, 3]
    print(f"Test 1: {countElements(a1)}") # Expected: 2

    a2 = [1, 1, 3, 3, 5, 5, 7, 7]
    print(f"Test 2: {countElements(a2)}") # Expected: 0