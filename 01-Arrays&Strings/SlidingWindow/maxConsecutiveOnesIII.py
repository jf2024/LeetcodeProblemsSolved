# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

def longestOnes(nums:list[int], k: int) -> int:
    left = 0
    ans = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    ans = longestOnes(nums1, k1)
    print(f"Longest subarray length is: {ans}") #should be 6


    nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k2 = 3
    ans2 = longestOnes(nums2, k2)
    print(f"Longest subarray length is: {ans2}") #should be 10
