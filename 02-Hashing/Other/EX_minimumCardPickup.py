from collections import defaultdict

def minimumCardPickup(cards: list[int]) -> int:
    """
    Given an integer array cards, find the length of the shortest subarray
    that contains at least one duplicate. If the array has no duplicates,
    return -1.

    Time Complexity: O(N) - despite the nested for loop, it can only iterate n times in total, iterating over 
    indices of elements from the array

    Space Complexity O(N)
    """
    groups = defaultdict(list)
    ans = float('inf')


    #populating hashmap, number is key and list of indexes are value
    for i in range(len(cards)):
        num = cards[i]
        groups[num].append(i)


    for key in groups:
        arr = groups[key] #grab our array
        for i in range(len(arr) - 1):  #inside array, calculate the pair of distances, need to do - 1 or we get an error for the last index
            ans = min(ans, arr[i + 1] - arr[i] + 1)
            #arr[i] = previous index
            #arr[i + 1] = current index

    return ans if ans < float('inf') else -1


def minimumCardPickUp(cards: list[int]) -> int: 
    """
    This Version has a slightly better space complexity
    We don't need to store all the indices, but only the most recent one that we saw for that number 
    """
    dic = defaultdict(int)
    ans = float('inf')

    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i - dic[cards[i]] + 1)
            #i = current index
            #dict[cards[i]] = previous index

        dic[cards[i]] = i   
        # will either add the new key (num) with the value of its index
        # or update the key with the most recent index 
    
    return ans if ans < float('inf') else -1


"""
Notice how both implementations utilize the current index - previous index + 1 
in different contexts
"""

if __name__ == "__main__":
    # Test 1
    c1 = [3, 4, 2, 3, 4, 7]
    print(f"Test 1: {minimumCardPickup(c1)}")
    # Expected: 4  (e.g., subarray [3, 4, 2, 3])

    # Test 2: No duplicates
    c2 = [1, 0, 5, 3]
    print(f"Test 2: {minimumCardPickup(c2)}")
    # Expected: -1

    # Test 3: Immediate duplicate
    c3 = [7, 7, 3, 4, 7]
    print(f"Test 3: {minimumCardPickup(c3)}")
    # Expected: 2  (subarray [7, 7])

    # Test 4: Duplicate further apart
    c4 = [1, 2, 1, 3, 4, 2]
    print(f"Test 4: {minimumCardPickup(c4)}")
    # One minimal example: [1, 2, 1] -> length 3, or [2, 1, 3, 4, 2] -> length 5
    # Expected: 3
