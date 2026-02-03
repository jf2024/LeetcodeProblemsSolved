from collections import defaultdict

def max_subarray_length(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k.

    The frequency of an element x is the number of times it occurs in an array.
    An array is called good if the frequency of each element in this array
    is less than or equal to k.

    Return the length of the longest good subarray of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Examples:
    - nums = [1,2,3,1,2,3,1,2], k = 2 -> 6
    - nums = [1,2,1,2,1,2,1,2], k = 1 -> 2
    - nums = [5,5,5,5,5,5,5], k = 4     -> 4


    Time Complexity: O(N)
        - n is the length of the nums array

    Space Complexity: O(N) 
        - n is the size of the input for our dictionary 
    """
    dic = defaultdict(int)

    ans = 0
    left = 0

    for right in range(len(nums)):
        dic[nums[right]] += 1

        while dic[nums[right]] > k:
            dic[nums[left]] -= 1
            if dic[nums[left]] == 0:
                del dic[nums[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans



def run_tests():
    test_cases = [
        # (nums, k, expected)
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
        ([5, 5, 5, 5, 5, 5, 5], 4, 4),
        ([1], 1, 1),
        ([1, 1, 1, 2], 2, 3),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = max_subarray_length(nums, k)
        print(f"Test case {i}: nums={nums}, k={k}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()
