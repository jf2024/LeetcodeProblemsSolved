# 2090. K Radius Subarray Averages
# link to problem: https://leetcode.com/problems/k-radius-subarray-averages/description/

def getAverages(nums: list[int], k: int) -> list[int]:
    """
    Builds and returns an array of k-radius averages.
    The window for index i is [i - k, i + k].
    
    Complexity Analysis (Target):
    - Time: O(n) where n is the length of nums.
    - Space: O(n) to store the prefix sum array and the output array.
    """
    # ---------------------------------------------------------
    # TODO: YOUR LOGIC HERE
    #
    pass

if __name__ == "__main__":
    # Test 1: Standard case
    n1, k1 = [7, 4, 3, 9, 1, 8, 5, 2, 6], 3
    print(f"Test 1: {getAverages(n1, k1)}") 
    # Expected Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    # Test 2: Radius 0
    n2, k2 = [100000], 0
    print(f"Test 2: {getAverages(n2, k2)}") 
    # Expected Output: [100000]

    # Test 3: Radius larger than array
    n3, k3 = [8], 100000
    print(f"Test 3: {getAverages(n3, k3)}") 
    # Expected Output: [-1]