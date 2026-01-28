from collections import defaultdict

def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Count how many characters in 'stones' exist in the 'jewels' string.
    Note: Letters are case-sensitive.

    Time Complexity: O(N + M)
        - N = nmber of stones
        - M = number of jewels

    Space Complexity: O(K)
        - K is number of unique stones
        - if its just english letters, can be O(1)
    """
    stones_count = defaultdict(int)

    for stone in stones:
        stones_count[stone] += 1

    total = 0
    for stone in jewels:
        total += stones_count[stone]

    return total


"""
VERSION 2 WITH A SET INSTEAD OF A DICTIONARY 
"""
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewel_set = set(jewels) # O(M) time to build
    total = 0
    
    for stone in stones: # O(N) time
        if stone in jewel_set: # O(1) lookup
            total += 1
            
    return total

"""
or just do this one liner here return sum(s in set(jewels) for s in stones)
"""

if __name__ == "__main__":
    print(f"Test 1: {numJewelsInStones('aA', 'aAAbbbb')}") # Expected: 3
    print(f"Test 2: {numJewelsInStones('z', 'ZZ')}")      # Expected: 0