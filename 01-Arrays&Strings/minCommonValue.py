def getCommon(nums1: list[int], nums2: list[int]) -> int:
    """
    Time Complexity: O(n + m) - n is array1 and m is array2, worst case we traverse both arrays once
    Space Complexity: O(1)
    """
    i = j = 0
    ans = -1 #set this to -1 since if both arrays dont have a common integer, return -1

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]: 
            # if the same integer, thats our answer and 
            # we break since we want the smallest integer value 
            # and the arrays are in increasing order so no point in checking
            ans = max(ans, nums1[i])
            return ans 

        elif nums1[i] < nums2[j]: 
            i += 1
        
        else: 
            j += 1

    return ans

    """
   1) Also a set implementation of this below

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Add the elements from nums1 to set1
        set1 = set(nums1)
        # Search for each element of nums2 in set1
        # Return the first common element found
        for num in nums2:
            if num in set1:
                return num
        # Return -1 if there are no common elements
        return -1

    2) Or this other set implementation
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)

        if common:
            return min(common)
        else: 
            return -1

    3) Can also do a binary search (go to the link for this problem if u wanna see, i didnt put it here)
    """

if __name__ == "__main__":
    # Test 1
    n1_1, n1_2 = [1, 2, 3], [2, 4]
    print(f"Test 1: {getCommon(n1_1, n1_2)}") # Expected: 2

    # Test 2
    n2_1, n2_2 = [1, 2, 3, 6], [2, 3, 4, 5]
    print(f"Test 2: {getCommon(n2_1, n2_2)}") # Expected: 2