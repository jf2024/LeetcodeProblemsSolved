def reverseWords(s: str) -> str:
    ans = []

    b = s.split()

    for word in b:
        for char in range(len(word) - 1, -1, -1):
            ans.append(word[char])
        ans.append(" ")

    ans = ans[:len(ans)-1]
    
    return "".join(ans)




if __name__ == "__main__":
    # Test 1
    s1 = "Let's take LeetCode contest"
    print(f"Test 1: {reverseWords(s1)}") # Expected: "s'teL ekat edoCteeL tsetnoc"

    # Test 2
    s2 = "Mr Ding"
    print(f"Test 2: {reverseWords(s2)}") # Expected: "rM gniD"