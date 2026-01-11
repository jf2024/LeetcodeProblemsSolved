# 344. Reverse String
# link to problem - https://leetcode.com/problems/reverse-string/description/

def reverseString(s: list[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



if __name__ == "__main__":
    # Test 1: Standard string
    input_s = ["h", "e", "l", "l", "o"]
    reverseString(input_s)
    print(f"Test 1 Result: {input_s}") 
    # Expected: ["o", "l", "l", "e", "h"]

    # Test 2: Even length
    input_s2 = ["H", "a", "n", "n", "a", "h"]
    reverseString(input_s2)
    print(f"Test 2 Result: {input_s2}") 
    # Expected: ["h", "a", "n", "n", "a", "H"]