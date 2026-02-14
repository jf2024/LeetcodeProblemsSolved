from collections import defaultdict

def word_pattern(pattern: str, s: str) -> bool:
    """
    Given a pattern and a string s, find if s follows the same pattern.
    Follow means a full match, such that there is a bijection between 
    a letter in pattern and a non-empty word in s.

    Time Complexity: O(N + M)
        - split traverses the string once (O(M)) time
        - zip runs for N interations (O(N)) time

    Space Complexity: O(N)
        - n number of unique words/characters are being stored

    Took heavy inspiration from the isIsomorphic Pattern
    """
    s_list = s.split(" ")

    if len(s_list) != len(pattern):
        return False
    
    patternToWord = defaultdict(str) #{a: dog, b: cat}
    wordToPattern = defaultdict(str) #{dog: a, cat: b}

    for letter, word in zip(pattern, s_list):
        if letter in patternToWord and patternToWord[letter] != word:
            return False

        if word in wordToPattern and wordToPattern[word] != letter:
            return False

        patternToWord[letter] = word
        wordToPattern[word] = letter

    return True

if __name__ == "__main__":
    test_cases = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("jquery", "jquery", False)
    ]
    
    for p, s, expected in test_cases:
        result = word_pattern(p, s)
        print(f"Pattern: {p:7} | String: {s:18} | Result: {str(result):5} | Passed: {result == expected}")
