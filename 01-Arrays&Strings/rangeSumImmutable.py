from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """
        We start the prefix sum with a leading 0 at first

        The reason why we do this is so that the first 'i' elements
        equate to prefix[i]

        Without this, would need to do prefix[left - 1] to get the range sum. Would 
        cause a 'index out of bounds' if our 'left' was 0. So we would need to write
        an if statement for that special case


        Example:
            - nums = [10, 20, 30]
            - prefix = [0, 10, 30, 60]

        Getting sum of index 0 to 1: (10 + 20 = 30)
        Formula: prefix[1 + 1] - prefix[0] = 30 - 0 = 30
        """
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        """
        Why is it right + 1? Remember that leading 0 to our prefix array, so everything
        is shifted by the right by one 

        prefix[right + 1] = sum of everything from the start up to right
        prefix[left] = sum of everything before the left
        """
        return self.prefix[right + 1] - self.prefix[left]

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    # Test 1
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(f"sumRange(0, 2): {obj.sumRange(0, 2)}") # Expected: 1
    print(f"sumRange(2, 5): {obj.sumRange(2, 5)}") # Expected: -1
    print(f"sumRange(0, 5): {obj.sumRange(0, 5)}") # Expected: -3