def combine(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Combines two sorted arrays into a single sorted array.
    
    Complexity Analysis:
    - Time: O(n + m) where n and m are the lengths of the two arrays.
      We iterate through every element in both arrays exactly once.
    - Space: O(n + m) to store the result in a new array.
    """

    ans = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


if __name__ == "__main__":
    # Test 1: Arrays of different lengths
    a1 = [1, 4, 7, 20]
    a2 = [3, 5, 6]
    print(f"Test 1: {combine(a1, a2)}") 
    # Expected: [1, 3, 4, 5, 6, 7, 20]

    # Test 2: One array is empty
    a3 = []
    a4 = [1, 2, 3]
    print(f"Test 2: {combine(a3, a4)}") 
    # Expected: [1, 2, 3]

    # Test 3: Arrays with duplicate values
    a5 = [1, 2, 2]
    a6 = [2, 4, 5]
    print(f"Test 3: {combine(a5, a6)}") 
    # Expected: [1, 2, 2, 2, 4, 5]