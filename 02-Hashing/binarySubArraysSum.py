from collections import defaultdict

"""
THE PREFIX SUM + HASHING PATTERN (The "Subarray Sum" Framework)

1. THE CORE LOGIC: THE "GAP" ANALOGY
   Think of the array as a path you are walking. 
   - 'curr' is your total distance from the starting line.
   - 'goal' is a specific distance you want a segment of that path to be.
   
   If you are currently at 10 miles (curr) and you want to find a 
   segment that is exactly 3 miles long (goal), you need to look 
   back and see how many times in the past you were at 7 miles.
   
   Equation: Previous_Sum = Current_Sum - Goal

2. WHY THE SUBTRACTION (curr - goal)?
   This pattern almost always involves subtraction because we are 
   looking for a "starting point" in our history. 
   - 'curr' contains the sum of the subarray we want PLUS some extra 
     prefix from the beginning.
   - By subtracting the 'goal', we calculate exactly how much that 
     "extra prefix" must have been.

3. WHY A DICTIONARY (Frequency Map)?
   In arrays with zeros or negative numbers, you can reach the 
   SAME prefix sum multiple times.
   Example: [1, 0, 0, 0] with goal 1.
   You hit the sum '1' at index 0. Then you stay at sum '1' for the 
   next three zeros. Each time you hit that sum again, it represents 
   a NEW unique subarray that satisfies the goal. 
   The dictionary tracks HOW MANY ways we could have started.

4. THE BASE CASE: counts[0] = 1
   We must initialize the map with 0:1 to represent the "empty" 
   prefix sum before the array starts. This ensures that if 
   (curr - goal) == 0, we correctly count the subarray that 
   starts from the very first element (index 0).

5. MENTAL TRIGGER:
   If a problem asks to "Count the number of subarrays..." and 
   sliding window feels difficult due to zeros or negative numbers, 
   immediately reach for: 
   Prefix Sum + Hash Map (curr - goal).
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
