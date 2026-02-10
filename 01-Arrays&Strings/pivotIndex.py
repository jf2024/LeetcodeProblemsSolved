def pivotIndex(nums: list[int]) -> int:
    """
    PREFIX SUM SOLUTION

    TIME: O(N)
    SPACE: O(N)
    """

    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    for i in range(len(nums)):
        left = prefix[i - 1] if i > 0 else 0
        right = prefix[-1] - prefix[i] 

        if left == right:
            return i
    
    return -1

def pivotIndex(nums: list[int]) -> int:
    """
    VERSION 2
    WITHOUT PREFIX SUM

    TIME: O(N)
    SPACE: O(1)
    """
    total_sum = sum(nums)
    left_sum = 0
        
    for i in range(len(nums)):
        # The right sum is everything else MINUS the current number
        right_sum = total_sum - left_sum - nums[i]
            
        if left_sum == right_sum:
            return i
            
        # Prepare the left_sum for the NEXT index
        left_sum += nums[i]
            
    return -1




if __name__ == "__main__":
    # Test 1
    n1 = [1, 7, 3, 6, 5, 6]
    print(f"Test 1: {pivotIndex(n1)}") # Expected: 3

    # Test 2
    n2 = [1, 2, 3]
    print(f"Test 2: {pivotIndex(n2)}") # Expected: -1

    # Test 3
    n3 = [2, 1, -1]
    print(f"Test 3: {pivotIndex(n3)}") # Expected: 0