from collections import Counter, defaultdict

def findLucky(arr: list[int]) -> int:
    """
    Given an array of integers arr, a lucky integer is an integer 
    that has a frequency in the array equal to its value.
    Return the largest lucky integer. If none exist, return -1.

    Time and Space Complexity: O(N)

    My original implementation
    Two passes
    """
    dic = defaultdict(int)
    ans = -1

    for num in arr:
        dic[num] += 1

    for key, value in dic.items():
        if key == value:
            ans = max(ans, key)

    return ans


if __name__ == "__main__":
    # Test Case 1
    a1 = [2, 2, 3, 4]
    print(f"Test 1: {findLucky(a1)}") # Expected: 2

    # Test Case 2
    a2 = [1, 2, 2, 3, 3, 3]
    print(f"Test 2: {findLucky(a2)}") # Expected: 3

    # Test Case 3
    a3 = [2, 2, 2, 3, 3]
    print(f"Test 3: {findLucky(a3)}") # Expected: -1