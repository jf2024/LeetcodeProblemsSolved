def find_isolated_numbers(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, find all the numbers x in nums such that:
    x + 1 is not in nums, and x - 1 is not in nums.
    Include each valid x only once in the final answer.

    Time and Space complexity: O(N)
    """
    set_nums = set(nums)
    ans = []

    for num in set_nums:
        if (num + 1 not in set_nums) and (num - 1 not in set_nums):
            ans.append(num)

    return ans

if __name__ == "__main__":
    # Test 1
    n1 = [1, 3, 5, 7]
    print(f"Test 1: {find_isolated_numbers(n1)}") 
    # Expected: [1, 3, 5, 7] (or any order)

    # Test 2
    n2 = [1, 2, 3, 5, 8, 9]
    print(f"Test 2: {find_isolated_numbers(n2)}") 
    # Expected: [5]

    # Test 3
    n3 = [10, 10, 12, 12, 11]
    print(f"Test 3: {find_isolated_numbers(n3)}") 
    # Expected: []

    # Test 4
    n4 = [4, 6, 8, 10]
    print(f"Test 4: {find_isolated_numbers(n4)}") 
    # Expected: [4, 6, 8, 10]