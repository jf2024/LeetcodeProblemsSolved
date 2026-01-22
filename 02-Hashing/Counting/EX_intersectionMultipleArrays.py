from collections import defaultdict

def intersection(nums: list[list[int]]) -> list[int]:
    """
    Given a 2D array nums where each nums[i] contains distinct integers,
    return a sorted array of numbers that appear in ALL arrays.
    """

    """
    Time Complexity: O(N * M + M log M) 
        - N * M to traverse all elements and populate/filter the map.
        - M log M to sort the final result (at most M elements).
    
    Space Complexity: O(N * M)
        - To store all unique elements in the hash map.
    """

    
    counts = defaultdict(int)
    ans = []

    # populating our dictionary here 
    for arrs in nums:
        for number in arrs:
            counts[number] += 1

    # my orginal way using .items(), but for this problem might be unnecessary
    # for key, values in counts.items():
    #     if values == len(nums):
    #         ans.append(key)


    for key in counts:
        if counts[key] == len(nums):
            ans.append(key)


    return sorted(ans)


if __name__ == "__main__":
    n1 = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    print(f"Test 1: {intersection(n1)}") 
    # Expected: [3, 4]

    n2 = [[1, 2, 3], [4, 5, 6]]
    print(f"Test 2: {intersection(n2)}") 
    # Expected: []
