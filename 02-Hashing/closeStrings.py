from collections import defaultdict

def close_strings(word1: str, word2: str) -> bool:
    """
    MY ORIGINAL IMPLEMENTATION

    TIME: O(N + k*log(K))
        - Counting Characters: You iterate through word1 and word2 (N elements each) 
            to build the initial maps → O(N).
        - Extracting Values: Creating a list from dictionary values takes O(K), 
            where K is the number of unique characters.
        - Sorting: This is the bottleneck. Sorting a list of size K takes O(KlogK).
        - Note: Since K is capped at 26 (English alphabet), this is technically linear in practice, 
            but O(KlogK) is the strictly accurate way to describe the sorting work.

    SPACE: O(K)
        - store up to k unique characters

    THINKING: 
        - i knew i had to use a hashmap in some capacity

        - my first approach was identifying that if the two words contain the same letters regardless of the 
        counts for each letter, that its possible to achieve the same word 

        - that failed so i then considered the counts of the letters, the counts need to be the same for both regardless
        of what that count is associated with
            - so for example
                - word1 can be a: 2, b: 1, c: 3 
                - word2 can be a: 1, b: 3, c: 2
                - the counts are the same in both dictionaries so all good there 

        - so then, combine those two requirements, both need to be true in order for it to be true, if one of those 
        condition fails, then return False 
    """
    if len(word1) != len(word2):
        return False
    
    word1_counts = defaultdict(int)
    word2_counts = defaultdict(int)

    # word1_set = set() #original implementation that solved it, dont need the sets, just check the keys
    # word2_set = set()

    for w in word1:
        word1_counts[w] += 1
        #word1_set.add(w)

    for w in word2:
        word2_counts[w] += 1
        #word2_set.add(w)

    return (word1_counts.keys() == word2_counts.keys()) and (sorted(list(word1_counts.values())) == sorted(list(word2_counts.values())))

def close_strings(word1: str, word2: str) -> bool:
    """
    VERSION 2 

    IMPROVED VERSION WITHOUT THE EXPLICIT SORTING (had to get some hlep from gemini but the 
    original thinking of the general solution is mine, just the final efficiency part)

    TIME: O(N + K)
        - first maps: O(N)
        - second maps: O(K)

    Space: O(K)
        - 4 maps but O(4k) is just O(K)
    """

    if len(word1) != len(word2):
        return False
    
    word1_counts = defaultdict(int)
    word2_counts = defaultdict(int)

    count1_counts = defaultdict(int)
    count2_counts = defaultdict(int)

    for w in word1: 
        word1_counts[w] += 1

    for w in word2: 
        word2_counts[w] += 1

    for counts in word1_counts.values():
        count1_counts[counts] += 1

    for counts in word2_counts.values():
        count2_counts[counts] += 1

    check_keys = word1_counts.keys() == word2_counts.keys()
    check_frequency_of_counts = count1_counts == count2_counts
    print(count1_counts)
    print(count2_counts)

    return check_keys and check_frequency_of_counts


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"word1": "abc", "word2": "bca", "expected": True},
        {"word1": "a", "word2": "aa", "expected": False},
        {"word1": "cabbba", "word2": "abbccc", "expected": True},
        {"word1": "uau", "word2": "ssx", "expected": False},
    ]

    print("--- Running Determine if Two Strings Are Close Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = close_strings(test["word1"], test["word2"])
        passed = result == test["expected"]
        print(f"Test {i}: word1='{test['word1']}', word2='{test['word2']}' | Result: {result} | Passed: {passed}")

if __name__ == "__main__":
    run_tests()