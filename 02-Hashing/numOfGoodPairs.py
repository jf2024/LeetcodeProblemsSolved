from collections import defaultdict
def num_identical_pairs(nums: list[int]) -> int:
    """
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100

    Time Complexity: O(N)
        - O(N) passing through the list the first time and O(N) passing through the dictionary
        - O(N) + O(N) = O(2N) which is just O(N)

    Space Complexity: O(N)
        - dictionary stores N keys

    Two pass approach - Version 1
    """
    dic = defaultdict(list)

    for i in range(len(nums)):
        dic[nums[i]].append(i)

    total = 0
    for key in dic:

        n = len(dic[key])
        pairs = int((n * (n - 1)) / 2)

        total += pairs

    return total

def num_identical_pairs(nums: list[int]) -> int:
        """
        Version 2:

        TWO PASS APPROACH
        A LITTLE BIT MORE OPTIMIZATION COMPARED TO THE ABOVE

        Instead of storing every index into a list, just count the number of times it appears
        and the value will be our length

        Same time and space complexity 
        """
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1

        total = 0
        for key in dic:

            n = dic[key]
            pairs = int((n * (n - 1)) / 2)

            total += pairs

        return total

def num_identical_pairs(nums: list[int]) -> int:
    """
    Version 3: ONE PASS SOLUTION

    THE PREFERRED VERSION
    
    This approach calculates the number of good pairs dynamically as we 
    iterate through the array. 
    
    Logic:
    When we encounter a number, the number of new 'good pairs' it can form 
    is equal to the count of times we have seen that same number previously. 
    By adding this count to our total before incrementing the frequency, 
    we effectively count all pairs (i, j) where i < j.

    The "trick" here is realizing that the n-th occurrence of a number creates n−1 new pairs.

    Example: nums = [1, 2, 3, 1, 1]
    1. '1': total_pairs += 0, counts = {1: 1}
    2. '2': total_pairs += 0, counts = {1: 1, 2: 1}
    3. '3': total_pairs += 0, counts = {1: 1, 2: 1, 3: 1}
    4. '1': total_pairs += 1, counts = {1: 2, 2: 1, 3: 1} (Pairs with 1st '1')
    5. '1': total_pairs += 2, counts = {1: 3, 2: 1, 3: 1} (Pairs with 1st & 2nd '1')
    Total = 3 pairs.

    Time Complexity: O(n)
    We traverse the list 'nums' exactly once. Each hash map operation 
    (lookup and insertion) takes O(1) time on average.

    Space Complexity: O(n)
    In the worst case where all elements in 'nums' are unique, the hash map 
    will store 'n' keys.
    """

    counts = defaultdict(int)
    total_pairs = 0

    for num in nums:
        total_pairs += counts[num]
        counts[num] += 1

    return total_pairs



def run_tests():
    test_cases = [
        # (nums, expected)
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([1, 1], 1),
        ([1, 2, 1, 2, 1], 4),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = num_identical_pairs(nums)
        passed = result == expected
        print(f"Test case {i}: nums={nums}, expected={expected}, got={result}, passed={passed}")


if __name__ == "__main__":
    run_tests()
