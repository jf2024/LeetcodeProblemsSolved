def reverseWords(s: str) -> str:
    """
    Time complexity: O(N)
    Space complexity: O(N) the ans var
    """
    ans = []

    b = s.split() #[word1, word2, etc...]

    for word in b:
        for char in range(len(word) - 1, -1, -1):
            ans.append(word[char])
        ans.append(" ")

    ans = ans[:len(ans)-1] #ans.strip() as well 
    
    return "".join(ans)


def reverseWordsLeetCodeTwoPointers(s: str) -> str:
    """
    Time complexity: O(N^2) because strings are immutable
    Space complexity: O(N) the words var
    """

    words = s.split()
    reversed_str = ""
    for word in words:
        # sequence[start : end : step] 
        reversed_str += word[::-1] + " "  #word[::-1] = start from the end and move left by 1 each time

    return reversed_str.strip()


def alternativeTwoPointers(s: str) -> str:
    """
    Time complexity: O(N) - traverse list once
    Space complexity: O(N) - the newlist var
    """

    newList = list(s)
    
    left = 0
    right = 0
    
    for i in range(len(newList)):
        if newList[i] == " " or i == len(newList) - 1: #if we hit an empty space or at the end of the list
            right = i - 1 if newList[i] == " " else i   #if empty, i-1, ELSE just i
            while left < right:
                newList[left], newList[right] = newList[right], newList[left] #switch the characters
                left += 1
                right -= 1
                
            left = i + 1    #set our left pointer index to the start of the next word after the space 
                
    return "".join(newList)




if __name__ == "__main__":
    s1 = "Let's take LeetCode contest"
    print(f"Test 1: {reverseWords(s1)}") # Expected: "s'teL ekat edoCteeL tsetnoc"

    s2 = "Mr Ding"
    print(f"Test 2: {reverseWords(s2)}") # Expected: "rM gniD"