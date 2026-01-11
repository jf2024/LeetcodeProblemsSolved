# Maximum Average SubArray I
# link to problem - https://leetcode.com/problems/maximum-average-subarray-i/description/

def findMaxAverage(nums: list[int], k:int) -> float:
    """
    Finds a contiguous subarray of length k with the maximum average value.
    
    Complexity Analysis:
    - Time: O(n) where n is the length of nums. We pass through the array twice 
      (once to build the window, once to slide it).
    - Space: O(1) as we only store the current and maximum sums.
    """
    curr = 0
    final_ans = 0

    for i in range(k):
        curr += nums[i]

    final_ans = curr / k

    for i in range(k, len(nums)):
        curr += nums[i]
        curr -= nums[i - k]

        final_ans = max(final_ans, curr / k)

    return final_ans

if __name__ == "__main__":
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    ans1 = findMaxAverage(nums1, k1)
    print(f"Array {nums1} max average with size {k1} is {ans1}")


    nums2 = [5]
    k2 = 1
    ans2 = findMaxAverage(nums2, k2)
    print(f"Array {nums2} max average with size {k2} is {ans2}")

