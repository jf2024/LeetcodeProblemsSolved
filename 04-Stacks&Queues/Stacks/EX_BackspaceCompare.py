def backspace_compare(s: str, t: str) -> bool:
    """
    MY ORIGINAL IMPLEMENTATION

    TIME: O(N + M)
        - iterate through s (O(N))
        - iterate through t (O(M))

    SPACE: O(N + M)
        - store all s characters (O(N))
        - store all t characters (O(M))

    VERSION 1
    """
    stack1 = []
    stack2 = []

    for i in range(len(s)):

        if stack1 and s[i] == '#':
                stack1.pop()

        elif s[i] != '#':
            stack1.append(s[i])


    for i in range(len(t)):
        if stack2 and t[i] == '#':
            stack2.pop()

        elif t[i] != '#':
            stack2.append(t[i])


    return stack1 == stack2


def backspace_compare(s: str, t: str) -> bool:
    """
    VERSION 2 USING TWO POINTERS
    """

    i = len(s) - 1
    j = len(t) - 1
    s_skip = 0
    t_skip = 0

    while i >=0 or j >= 0: #while either string has characters left 

        while i >= 0:   #find valid 's' char
            if s[i] == '#':
                s_skip += 1
                i -= 1
            elif s_skip > 0:
                s_skip -= 1
                i -= 1
            else:
                break
        
        while j >= 0:   #find valid 'j' char
            if t[j] == "#":
                t_skip += 1
                j -= 1
            elif t_skip > 0:
                t_skip -= 1
                j -= 1
            else:
                break

        # if both are valid indices, compare the characters
        if i >= 0 and j >= 0:
            if s[i] != t[j]:    #if not equal, then return false even if the indices are the same
                return False
            
        elif (i >= 0) != (j >= 0): #if one is empty and the other isnt, not equal
            return False
        
        i -= 1
        j -= 1

    return True




def run_tests():
    test_cases = [
        {"s": "ab#c", "t": "ad#c", "expected": True},
        {"s": "ab##", "t": "c#d#", "expected": True},
        {"s": "a#c", "t": "b", "expected": False},
        {"s": "a##c", "t": "#a#c", "expected": True},
        {"s": "xywrrmp", "t": "xywrrmu#p", "expected": True},
    ]

    print("--- Running Backspace String Compare Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = backspace_compare(test["s"], test["t"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: s='{test['s']}', t='{test['t']}' | Result={result} | Expected={test['expected']} | {status}")

if __name__ == "__main__":
    run_tests()