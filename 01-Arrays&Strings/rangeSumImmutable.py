from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # TODO: Implement initialization
        pass

    def sumRange(self, left: int, right: int) -> int:
        # TODO: Implement range query
        pass

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    # Test 1
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(f"sumRange(0, 2): {obj.sumRange(0, 2)}") # Expected: 1
    print(f"sumRange(2, 5): {obj.sumRange(2, 5)}") # Expected: -1
    print(f"sumRange(0, 5): {obj.sumRange(0, 5)}") # Expected: -3