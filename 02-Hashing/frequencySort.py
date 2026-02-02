from collections import Counter
def frequencySort(s: str) -> str:
    """
    Given a string s, sort it in decreasing order based on the 
    frequency of the characters.

    Time Complexity: O(N + K log K)
        - counting: Counter(s) takes O(N) because we look at every character once
        - sorting: number of items is K (number of unique characters) so O(K log k)
        - building string: O(N)
        - so the total would be O(N + K log K)
    """
    a = Counter(s)
    str_list = []

    string_tuples = a.items()
    #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    sorted_tups = sorted(string_tuples, key=lambda tup: tup[1], reverse=True)

    for tup in sorted_tups:
        str_list.append(tup[0] * tup[1])

    return "".join(str_list)


def frequencySort(s: str) -> str:
    """
    VERSION 2
    - Instead of the sorted step from above, there is a function/method called most_common that 
    does it for us
    - The time and space complexity remain the same though
    """
    # 1. Count frequencies O(N)
    counts = Counter(s)
    
    # 2. most_common() returns sorted tuples: [('c', 3), ('a', 3)...]
    # This is O(K log K)
    sorted_tups = counts.most_common()
    
    # 3. Build string O(N)
    res = []
    for char, freq in sorted_tups:
        res.append(char * freq)
        
    return "".join(res)

def frequencySort(s: str) -> str:
    """
    Version 3

    This is a bucket sort implementation
    Instead of comparing frequencies (which takes O(K log K)), we treat 
    frequencies as array indices. Since array indices are inherently 
    ordered, walking the array from N down to 1 gives us the sorted 
    order automatically in O(N) time.

    You can only use this "natural sort" trick when:
        The range of values is finite and known: Here, the max frequency is exactly N (the string length).
        The values are integers: You can't have an array index of 2.5 or "apple".

    Time Complexity: O(N) - doing no sorting, using array indices as a "natural" sort since frequencies can't exceed
    N, its efficient 

    Same space complexity as the other two above
    """
    n = len(s)
    counts = Counter(s)

    # create buckets: an array of lists
    # index 0 to N (N + 1 size)
    buckets = [[] for _ in range(n + 1)] #so it would look like this for example: [[], [], [], [], []]

    # putting characters into bucket corresponding to their frequency
    for char, freq in counts.items():
        buckets[freq].append(char)

    print(buckets)


    # building string by iterating buckets backwards
    res = []
    for freq in range(n, 0, -1):
        for char in buckets[freq]:
            res.append(char * freq)

    return "".join(res)


if __name__ == "__main__":
    s1 = "tree"
    print(f"Test 1: {frequencySort(s1)}") # Expected: "eert" or "eetr"

    s2 = "cccaaa"
    print(f"Test 2: {frequencySort(s2)}") # Expected: "aaaccc" or "cccaaa"

    s3 = "Aabb"
    print(f"Test 3: {frequencySort(s3)}") # Expected: "bbAa" or "bbaA"