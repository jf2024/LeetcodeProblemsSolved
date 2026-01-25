from collections import defaultdict

def maxNumberOfBalloons(text: str) -> int:
    """
    Return the maximum number of instances of the word "balloon" 
    that can be formed from text.

    Time Complexity: O(N) - iterate through text exactly once 
    Space complexity: O(1) - despite using hash map, we only store 5 unique keys 
    """
    
    counts = defaultdict(int)

    for c in text:
        if c in 'balon':
            counts[c] += 1

    return min(
          counts['b'], 
          counts['a'], 
          counts['l'] // 2, 
          counts['o'] // 2, 
          counts['n']
      )
            
if __name__ == "__main__":
    t1 = "nlaebolko"
    print(f"Test 1: {maxNumberOfBalloons(t1)}") 
    # Expected: 1

    t2 = "loonbalxballpoon"
    print(f"Test 2: {maxNumberOfBalloons(t2)}") 
    # Expected: 2

    t3 = "leetcode"
    print(f"Test 3: {maxNumberOfBalloons(t3)}") 
    # Expected: 0