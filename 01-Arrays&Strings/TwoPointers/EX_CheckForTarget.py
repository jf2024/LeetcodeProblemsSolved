def check_for_target(nums: list[int], target: int) -> bool:
    """
    Determines if a pair of numbers exists in a sorted array that sums to a target.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of the array. Each element is visited at most once.
    - Space: O(1) as we only use two integer pointers regardless of input size.
    """

    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]

        if curr == target:
            return True
        elif curr > target:
            right -= 1
        else:
            left += 1

    return False

if __name__ == "__main__":
    # Test 1: Pair exists (4 + 9 = 13)
    nums1 = [1, 2, 4, 6, 8, 9, 14, 15]
    target1 = 13
    print(f"Test 1 (Target {target1}): {check_for_target(nums1, target1)}") # Expected: True

    # Test 2: Pair does not exist
    nums2 = [1, 2, 4, 6, 8, 9, 14, 15]
    target2 = 50
    print(f"Test 2 (Target {target2}): {check_for_target(nums2, target2)}") # Expected: False

    # Test 3: Smallest possible pair
    nums3 = [5, 10]
    target3 = 15
    print(f"Test 3 (Target {target3}): {check_for_target(nums3, target3)}") # Expected: True