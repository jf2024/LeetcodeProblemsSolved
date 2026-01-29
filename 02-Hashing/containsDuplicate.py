def containsDuplicate(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice 
    in the array, and return false if every element is distinct.
    """
    nums_set = set()

    for num in nums:
        if num in nums_set:     #if number is in set, then just return True
            return True
        else:
            nums_set.add(num)   #add to set 
        
    return False    #will only reach this point if every element is unique


if __name__ == "__main__":
    n1 = [1, 2, 3, 1]
    print(f"Test 1: {containsDuplicate(n1)}") # Expected: True

    n2 = [1, 2, 3, 4]
    print(f"Test 2: {containsDuplicate(n2)}") # Expected: False

    n3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Test 3: {containsDuplicate(n3)}") # Expected: True