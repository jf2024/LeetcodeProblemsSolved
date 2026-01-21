def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    min_answer = float('inf')
    inf = float('inf')
    left = 0
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_answer = min(min_answer, right - left + 1)
            total -= nums[left]
            left += 1

    return min_answer if min_answer != inf else 0


if __name__ == "__main__":
    t1, n1 = 7, [2, 3, 1, 2, 4, 3]
    print(f"Test 1: {minSubArrayLen(t1, n1)}") # Expected: 2

    t2, n2 = 4, [1, 4, 4]
    print(f"Test 2: {minSubArrayLen(t2, n2)}") # Expected: 1

    t3, n3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Test 3: {minSubArrayLen(t3, n3)}") # Expected: 0

    t4, n4 = 11, [1,2,3,4,5]
    print(f"Test 4: {minSubArrayLen(t4, n4)}") # Expected: 3