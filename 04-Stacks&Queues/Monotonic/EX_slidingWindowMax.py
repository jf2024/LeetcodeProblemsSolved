from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Time: O(N)
        - n is the size of nums

    Space: O(k)
        - deque can't grow beyond that size of n
    """
    ans = []
    queue = deque() #stores indices

    for i in range(len(nums)):

        # maintain the monotonic decreasing, similar to the daily temp problem
        # elements in the deque smaller then the current one have no chance of being 
        #   the max so just delete
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i) #and we add our index to the queue

        # queue[0] = index of the maxium element
        # if the condition is true, then our index of the max element is outside of the window
            # so we need to pop it 
        if queue[0] + k == i: 
            queue.popleft()


        # add our answer after reaching the size of the window size
        if i >= k - 1:
            ans.append(nums[queue[0]])

    return ans

"""
HIGH LEVEL EXPLANATION IN MY OWN WORDS

so the first part isnt that much different from the daily temperatures problem
we check if our queue is not empty and if our current number is greater then the most 
recent element of our queue, we need to pop to maintain that monotonic decreasing


after that while loop, we can safely add our index (normal behavrion from our daily temp problem)


however, we need to check 2 additional things
the first being is that our index (queue[0]) is still within our window, 
if its not within our window, we need to pop that

after that, we add to our answer after we reach the size of our window size 
(and for every iteration after we add but for the first potential couple of iterations we dont add 
yet since our window size hasnt grown yet) 
"""



# --- Test Cases ---
def run_tests():
    test_cases = [
        {
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
            "expected": [3, 3, 5, 5, 6, 7]
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1]
        },
        {
            "nums": [7, 2, 4],
            "k": 2,
            "expected": [7, 4]
        },
        {
            "nums": [9, 11, 8, 5, 7, 10],
            "k": 3,
            "expected": [11, 11, 8, 10]
        }
    ]

    print("--- Running Sliding Window Maximum Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = max_sliding_window(test["nums"], test["k"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: nums={test['nums']}, k={test['k']}")
        print(f"Result:   {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status:   {status}\n")

if __name__ == "__main__":
    run_tests()