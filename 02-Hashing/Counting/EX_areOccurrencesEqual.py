from collections import defaultdict

def areOccurrencesEqual(s: str) -> bool:
    """
    Given a string s, return True if all characters appear the 
    same number of times, False otherwise.

    Time Complexity: O(N) - looing through the string once to count characters
    Space Complexity: O(K) 
        - Where K is the number of unique characters
        - if limited to lowercase english letters, would be O(1) as K <= 26
    """
    counts = defaultdict(int)

    for char in s:
        counts[char] += 1


    ## my original way below with an extra for loop
    # see = set()
    # for key in counts:
    #     see.add(counts[key])

    # return len(see) == 1


    ## can just get our values and convert to a set and check if equal to 1 
    frequencies = counts.values()
    return len(set(frequencies)) == 1


if __name__ == "__main__":
    s1 = "abacbc"
    print(f"Test 1: {areOccurrencesEqual(s1)}") 
    # Expected: True (All chars appear 2 times)

    s2 = "aaabb"
    print(f"Test 2: {areOccurrencesEqual(s2)}") 
    # Expected: False ('a' appears 3x, 'b' appears 2x)

    s3 = "vvvvvv"
    print(f"Test 3: {areOccurrencesEqual(s3)}") 
    # Expected: True (Only one char, so frequencies are equal)