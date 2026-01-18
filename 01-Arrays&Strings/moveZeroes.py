def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """


    ## my original solution
    # left = 0 
    # right = 0
    # n = len(nums)

    # while right < n:
    #     if nums[left] != 0:
    #         left += 1
    #         right += 1

    #     elif nums[right] != 0:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right += 1
        
    #     else:
    #         right += 1


    """
    The Nicer way right here
    """

    left = 0
    for right in range(len(nums)): #the right will look for every non-zero
        if nums[right] != 0: 
            nums[left], nums[right] = nums[right], nums[left] #swap the non-zero with the left position
            left += 1

# More explanation for this code

# Why this is true (step-by-step logic)
# Let’s reason it out

    # left only advances when a non-zero is placed
    # Everything before left is guaranteed non-zero
    # right moves forward one step at a time

    # Now assume left < right
    # This means:
    # right has already scanned indices [left, right)
    # If there had been a non-zero in that range, left would have moved forward

    # Therefore:
    # All elements between left and right - 1 must be zero

# Indices < left --> contain all non-zero elements in correct order
# Indices [left, right) -->  contain only zeros
# Indices >= right --> are unprocessed

if __name__ == "__main__":
    # Test 1
    n1 = [0, 1, 0, 3, 12]
    moveZeroes(n1)
    print(f"Test 1: {n1}") # Expected: [1, 3, 12, 0, 0]

    # Test 2
    n2 = [0]
    moveZeroes(n2)
    print(f"Test 2: {n2}") # Expected: [0]

    n3 = [1, 1, 1, 0, 1]
    moveZeroes(n3)
    print(f"Test 2: {n3}")