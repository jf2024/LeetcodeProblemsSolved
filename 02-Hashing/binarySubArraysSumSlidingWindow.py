"""
WHY SLIDING WINDOW?
It can work because there are no negative numbers (the sum is non-decreasing).
However, to handle the zeros, we must use the "At Most K" logic. 
It is more memory efficient (O(1) space) but the logic is more abstract.
"""

def sliding_window_at_most(nums: list[int], goal: int) -> int:
    """
    Helper function to count all subarrays where the sum is <= goal.
    
    Why 'At Most'? 
    Counting 'Exactly K' is hard with zeros because the window sum stays 
    the same even when the window size changes. 'At Most' is easy because 
    for every valid window [start, end], the number of valid subarrays 
    ending at 'end' is exactly the length of the window (end - start + 1).
    """
    if goal < 0:
        return 0

    start, current_sum, total_count = 0, 0, 0

    for end in range(len(nums)):
        current_sum += nums[end]

        # The 'start <= end' check:
        # This is a safety guard. If goal were somehow negative (which we handle above), 
        # current_sum > goal would always be true, and 'start' would move past 'end'.
        # It ensures our window boundaries stay physically possible.
        while start <= end and current_sum > goal:
            current_sum -= nums[start]
            start += 1

        # Every subarray ending at 'end' and starting between 'start' and 'end' 
        # is a valid subarray with sum <= goal.
        total_count += end - start + 1

    return total_count

def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    """
    Calculates the number of subarrays with a sum EXACTLY equal to goal.
    
    The Logic (Exact = At Most K - At Most K-1):
    To get the count of subarrays that sum to exactly 2, we take:

    (Total subarrays that sum to 0, 1, or 2) 
    MINUS 
    (Total subarrays that sum to 0 or 1)
    
    Result: Only the subarrays that sum to exactly 2 remain.
    
    This trick allows us to use Sliding Window (O(1) space) even 
    when the presence of zeros makes 'Exact K' logic messy.

    """
    return sliding_window_at_most(nums, goal) - sliding_window_at_most(nums, goal - 1)

