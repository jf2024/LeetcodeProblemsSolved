from collections import deque

def longest_subarray(nums: list[int], limit: int) -> int:
    """
    TIME: O(N)
        - every number is pushed into each deque at most once
        - every number is popped from each deque at most once
        - left pointer only moves forward 
        - 4n operations but thats just O(N)

    SPACE: O(N)
    """

    increasing = deque()    #will always hold the minimum element at the front 
    decreasing = deque()    #will always hold the max element at the front

    left = 0
    ans = 0

    for right in range(len(nums)):

        #maintain our monotonic property like in the previous two examples
        while increasing and increasing[-1] > nums[right]:
            increasing.pop()

        while decreasing and decreasing[-1] < nums[right]:
            decreasing.pop()

        increasing.append(nums[right])
        decreasing.append(nums[right])

        #if our window property breaks, bigger then limit, need to move our left 
        while decreasing[0] - increasing[0] > limit:
            if nums[left] == decreasing[0]:
                decreasing.popleft()

            if nums[left] == increasing[0]:
                increasing.popleft()

            left += 1

        # window property is fine, so get the length of our subarray 
        ans = max(ans, right - left + 1)

    return ans


"""
HIGH LEVEL UNDERSTANDING/EXPLANATION

so we have two deques, one for increasing and the other for decreasing
our first two while loops is to ensure our deques keep that property of 
increasing or decreasing and we pop accordingly

once we know both deques are good, we can add our number to both

we then have to check if our largest and smallest number is bigger then the limit, 
if it is, then we violate that condition and we need to move left
the way to do that for this problem is popping the left-most number from either or both of the deques and add left +1 after


and then we have a valid window which is our standard right - left + 1 for the length of the subarray and we return 
"""

# --- Test Cases ---
def run_tests():
    test_cases = [
        {
            "nums": [8, 2, 4, 7],
            "limit": 4,
            "expected": 2
        },
        {
            "nums": [10, 1, 2, 4, 7, 2],
            "limit": 5,
            "expected": 4
        },
        {
            "nums": [4, 2, 2, 2, 4, 4, 2, 2],
            "limit": 0,
            "expected": 3
        },
        {
            "nums": [1, 5, 6, 7, 8, 10, 6, 5, 6],
            "limit": 4,
            "expected": 5
        }
    ]

    print("--- Running Longest Continuous Subarray Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = longest_subarray(test["nums"], test["limit"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: limit={test['limit']}, nums={test['nums']}")
        print(f"Result:   {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status:   {status}\n")

if __name__ == "__main__":
    run_tests()