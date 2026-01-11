# 977. Squares of a Sorted Array
# link to problemhttps://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(nums:list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1

    ans = [0] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        if abs(nums[left]) < (nums[right]):
            ans[i] = nums[right] ** 2
            right -= 1
        else:
            ans[i] = nums[left] ** 2
            left += 1

    return ans

"""
Second way down below
"""
def sortedSquares(nums:list[int]) -> list[int]:
    return sorted(x * x for x in nums)
    

if __name__ == "__main__":
    input_s = [-4, -1, 0, 3, 10]
    ans = sortedSquares(input_s)
    print(f"After Sorting: {ans}") 

    input2 = [-7, -3, 2, 3, 11]
    ans2 = sortedSquares(input2)
    print(f"After sorting input2: {ans2}")