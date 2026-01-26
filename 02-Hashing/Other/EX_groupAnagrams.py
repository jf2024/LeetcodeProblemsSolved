from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together.
    Return a list of groups, where each group is a list of strings
    that are anagrams of each other.

    Time Complexity: O(N * Klog(K)) 
        - N = number of strings in list
        - K = avarage length of word and with the sorting, takes K * log(K) time 
    Space Complexity: O(N * K) to store all strings in the dictionary

    You can make the time complexity O(N * K) with counting (can look it up or ask gemini or chat) 
    """
    groups = defaultdict(list)

    for words in strs:
        key = "".join(sorted(words))    #if we just do sorted(words), will return ['a', 'b', 't'], so need the join to make it back to a string
        groups[key].append(words)       #create key if not found with empty list as value, or if key found, append it to the list already

    return list(groups.values())


if __name__ == "__main__":
    c1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Test 1: {groupAnagrams(c1)}")
    # Expected (order of groups and elements may vary):
    # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    c2 = [""]
    print(f"Test 2: {groupAnagrams(c2)}")
    # Expected: [[""]]

    c3 = ["a", "b", "a"]
    print(f"Test 3: {groupAnagrams(c3)}")
    # Expected: [["a", "a"], ["b"]]
