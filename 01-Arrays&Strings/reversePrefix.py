def reversePrefix(word: str, ch: str) -> str:
    """
    My original implementation
    """
    if ch not in word:
        return word
    
    window = []
    answer = []
    start = 0
    for i in range(len(word)):
        if word[i] == ch:
            start = i + 1
            window.append(word[i])
            break
        else:
            window.append(word[i])
        
        
    while len(window) > 0:
        answer.append(window.pop())

    for i in range(start, len(word)):
        answer.append(word[i])
    
    return "".join(answer)

def twoPointersReverse(word: str, ch:str) -> str:
    """
    Two pointers solution
    First find the target index
    then do the two pointers to reverse it 
    """
    if ch not in word:
        return word
    
    word_list = list(word)
    n = len(word_list)

    start = 0
    end = 0

    #first finding that target index
    for i in range(n):
        if word_list[i] == ch:
            end = i
            break

    #then do the reverse
    while start < end:
        word_list[start], word_list[end] = word_list[end], word_list[start]
        start += 1
        end -= 1

    return "".join(word_list)


# putting the while loop inside of the for loop
def twoPointersAlternative(word: str, ch:str) -> str:
    """
    Two pointers solution 
    the while loop inside of our for loop instead of outside like above
    """
    result = list(word)
    left = 0

    for right in range(len(word)):
        if result[right] == ch:

            while left < right:
                result[right], result[left] = result[left], result[right]
                left += 1
                right -= 1

            return "".join(result) #after our while loop is done, can just return 
        
    return word #return the word if we never hit that other condition



if __name__ == "__main__":
    w1, c1 = "abcdefd", "d"
    print(f"Test 1: {reversePrefix(w1, c1)}") # Expected: "dcbaefd"

    w2, c2 = "xyxzxe", "z"
    print(f"Test 2: {twoPointersReverse(w2, c2)}") # Expected: "zxyxxe"

    w3, c3 = "abcd", "z"
    print(f"Test 3: {reversePrefix(w3, c3)}") # Expected: "abcd"