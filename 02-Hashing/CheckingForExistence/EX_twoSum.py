def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of two numbers such that they add up to target.
    You cannot use the same index twice.

    Time Complexity: O(N) 
    Space complexity: O(N)
    """
    hash_map = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in hash_map: #this operation is O(1)
            return [i, hash_map[complement]] #return the indices
        
        hash_map[num] = i #store the number as the key, index is the value 


    return [-1, -1] #couldnt find a pair that matches the target


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 3, 7], 10),
    ]

    for nums, target in test_cases:
        print(f"nums={nums}, target={target} -> {two_sum(nums, target)}")
