from collections import defaultdict

def largestUniqueNumber(nums: list[int]) -> int:
    """
    Find the largest integer that only occurs once.

    Time and Space Complexity: O(N)
    Time explanation: one pass to count all N numbers and one pass to check frequencies 
    """
    ans = -1
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    for key in counts:
        if counts[key] == 1:
            ans = max(ans, key)
    
    return ans

if __name__ == "__main__":
    n1 = [5,7,3,9,4,9,8,3,1]
    print(f"Test 1: {largestUniqueNumber(n1)}") 
    # Expected: 8

    n2 = [9,9,8,8]
    print(f"Test 2: {largestUniqueNumber(n2)}") 
    # Expected: -1