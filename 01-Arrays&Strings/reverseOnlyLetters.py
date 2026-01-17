def reverseOnlyLetters(s: str) -> str:
    """
    Time Complexity: O(N) going through it once
    Space Complexity: O(N) creating list
    """
    letters = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

    left = 0
    right = len(s) - 1

    s = list(s)
    while left < right: 
        if s[left].lower() not in letters:
            left += 1
        elif s[right].lower() not in letters:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return "".join(s)


    """
    #Could have also done the following instead of building the letters list
    #and useing the built in isalpha

    left = 0
    right = len(s) - 1

    s = list(s)
    
    while left < right: 
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return "".join(s)
    """

def usingStackReverse(S: str) -> str:
    letters = [c for c in S if c.isalpha()] #our letters stack, (Last in - First Out)
    ans = []

    for c in S:
        if c.isalpha():
            ans.append(letters.pop()) #if we see a letter, pop the last element from our stack
        else:
            ans.append(c) #if not a letter, just add the symbol and move on 
    
    return "".join(ans) #convert back to a string


if __name__ == "__main__":
    s1 = "ab-cd"
    print(f"Test 1: {reverseOnlyLetters(s1)}") # Expected: "dc-ba"

    s2 = "a-bC-dEf-ghIj"
    print(f"Test 2: {reverseOnlyLetters(s2)}") # Expected: "j-Ih-gfE-dCba"

    s3 = "Test1ng-Leet=code-Q!"
    print(f"Test 3: {reverseOnlyLetters(s3)}") # Expected: "Qedo1ct-eeL=tseT-n!"