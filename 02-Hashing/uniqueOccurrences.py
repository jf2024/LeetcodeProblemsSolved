from collections import Counter, defaultdict

def uniqueOccurrences(arr: list[int]) -> bool:
    """
    Given an array of integers arr, return True if the number of occurrences 
    of each value in the array is unique, or False otherwise.

    Original Implementation
    Time and Space is O(N)
    """

    dic = defaultdict(int)

    for num in arr:
        dic[num] += 1

    freq_set = set(dic.values())

    return len(freq_set) == len(dic.values())


def uniqueOccurrences(arr: list[int]) -> bool:
    """
    Given an array of integers arr, return True if the number of occurrences 
    of each value in the array is unique, or False otherwise.

    """

    dic = defaultdict(int)

    for num in arr:
        dic[num] += 1

    seen_freqs = set()

    for freq in dic.values():
        if freq in seen_freqs:
            return False
        
        seen_freqs.add(freq)
        
    return True


if __name__ == "__main__":
    # Test Case 1
    a1 = [1, 2, 2, 1, 1, 3]
    print(f"Test 1: {uniqueOccurrences(a1)}") # Expected: True

    # Test Case 2
    a2 = [1, 2]
    print(f"Test 2: {uniqueOccurrences(a2)}") # Expected: False

    # Test Case 3
    a3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(f"Test 3: {uniqueOccurrences(a3)}") # Expected: True