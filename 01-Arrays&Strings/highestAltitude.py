def largestAltitude(gain: list[int]) -> int:
    """
    Time Complexity: O(N) - iterate over every integer in the list once

    Space Complexity: O(1) - only need two variables
    """
    ans = 0 
    curr = 0
    for n in gain:

        curr += n
        ans = max(curr, ans)

    return ans


if __name__ == "__main__":
    # Test 1
    g1 = [-5, 1, 5, 0, -7]
    print(f"Test 1: {largestAltitude(g1)}") # Expected: 1

    # Test 2
    g2 = [-4, -3, -2, -1, 4, 3, 2]
    print(f"Test 2: {largestAltitude(g2)}") # Expected: 0