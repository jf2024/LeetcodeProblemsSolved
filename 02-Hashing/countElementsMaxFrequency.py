from collections import defaultdict

def maxFrequencyElements(nums: list[int]) -> int:
    """
    You are given an array nums consisting of positive integers.
    Return the total frequencies of elements in nums such that 
    those elements all have the maximum frequency.

    My original implementation here
    """
    dic = defaultdict(int)

    for num in nums:
        dic[num] += 1

    max_freq = max(dic.values())

    counts = 0
    for freq in dic.values():
        if freq == max_freq:
            counts += freq

    return counts

#my original implementation does it in two passes, also a bit janky
#theres a way to do one pass through, can look at the last solution (solution 3) on leetcode below:
#https://leetcode.com/problems/count-elements-with-maximum-frequency/editorial/?envType=problem-list-v2&envId=ajcqwr0m
#and below is the one pass

"""
def maxFrequencyElements(nums: list[int]) -> int:
    counts = defaultdict(int)
    max_freq = 0
    total_max_freq_elements = 0

    for num in nums:
        counts[num] += 1
        current_freq = counts[num]

        # Case 1: We found a frequency higher than our current record
        if current_freq > max_freq:
            max_freq = current_freq
            # Everything we counted before is no longer the "max," 
            # so we reset the total to the new max frequency.
            total_max_freq_elements = current_freq

        # Case 2: This number just TIED the current record
        elif current_freq == max_freq:
            # Add this frequency to our total count
            total_max_freq_elements += current_freq

    return total_max_freq_elements
"""


if __name__ == "__main__":
    # Test Case 1
    n1 = [1, 2, 2, 3, 1, 4]
    print(f"Test 1: {maxFrequencyElements(n1)}") # Expected: 4

    # Test Case 2
    n2 = [1, 2, 3, 4, 5]
    print(f"Test 2: {maxFrequencyElements(n2)}") # Expected: 5