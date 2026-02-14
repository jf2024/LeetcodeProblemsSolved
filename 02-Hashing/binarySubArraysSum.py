from collections import defaultdict

"""
THE PREFIX SUM + HASHING PATTERN (The "Subarray Sum" Framework)

HOW THE CODE PLAYS ITS PART (Line-by-Line inside of the for loop):

1. curr += num
   - YOUR POSITION: This moves you further down the path. You are 
     calculating the total sum from the very beginning to here.

2. ans += counts[curr - goal]
   - THE LOOKBACK: You are asking, "How many times in the past was I 
     at a distance that is exactly 'goal' miles behind me?"
   - We add the FREQUENCY because if we were at that distance 3 times 
     before, there are 3 different starting points that create 
     3 different valid subarrays ending NOW.

3. counts[curr] += 1
   - THE RECORD: You are marking this spot on your map. You don't 
     use this mark for the current index (to avoid matching with 
     yourself), but you leave it there for FUTURE indices to find.

EXAMPLE TRACE: nums = [1, 0, 1], goal = 1
- At index 0 (num=1, curr=1): 
    Lookback 0 (1-1). ans becomes 1. Map: {0:1, 1:1}
- At index 1 (num=0, curr=1): 
    Lookback 0 (1-1). ans becomes 2. Map: {0:1, 1:2} 
    (Note: curr didn't change, but we found a new subarray [1, 0])
- At index 2 (num=1, curr=2): 
    Lookback 1 (2-1). We see '1' appeared TWICE in the past. 
    ans += 2. Total ans = 4.
"""


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    """
    Given a binary array nums and an integer goal, return the number of 
    non-empty subarrays with a sum equal to goal.

    Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - nums[i] is either 0 or 1.
    - 0 <= goal <= nums.length

    
    Time Complexity: O(N) because we iterate the array once
    Space Complexity: O(N) because in worst case (array is all positve numbers), every prefix sum would be unique and stored in the hash map


    Struggled a lot with this problem...........
    """

    counts = defaultdict(int)
    counts[0] = 1 #base case: prefix sum of 0 exists before we start (our empty subarray)
    curr = ans = 0

    for num in nums:
        curr += num     #updaing our prefix sum 
        ans += counts[curr - goal] #check if curr - k exists in our dictionary, if so add and if not, would just be 0 

        counts[curr] += 1 #then add that current prefix sum to the dictionary 

    return ans


def run_tests():
    test_cases = [
        # (nums, goal, expected)
        ([1, 0, 1, 0, 1], 2, 4),
        ([0, 0, 0, 0, 0], 0, 15),
        ([1, 1, 1, 1, 1], 3, 3),
        ([0, 0, 0], 0, 6),
    ]

    for i, (nums, goal, expected) in enumerate(test_cases, 1):
        result = num_subarrays_with_sum(nums, goal)
        passed = result == expected
        print(f"Test case {i}: nums={nums}, goal={goal}, expected={expected}, got={result}, passed={passed}")


if __name__ == "__main__":
    run_tests()
