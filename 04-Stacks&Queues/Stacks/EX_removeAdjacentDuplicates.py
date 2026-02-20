def remove_duplicates(s: str) -> str:
    """
    Time: O(N)
        - visiting each character once

    Space: O(N)
        - in the worst case, our stack will grow to the size of the string

    MY ORIGINAL IMPLEMENTATION
    """
    stack = []

    for letter in s: 
        if len(stack) == 0:
            stack.append(letter)

        elif letter == stack[-1]:
            stack.pop()
        else:

            stack.append(letter)

    return "".join(stack)

def remove_duplicates(s: str) -> str:
    """
    VERSION TWO 

    PRETTY MUCH THE SAME AS THE ABOVE BUT "CLEANER" 
    """
    stack = []

    for character in s: 
        if stack and stack[-1] == character: 
            stack.pop()
        else:
            stack.append(character)

    return "".join(stack)


def run_tests():
    test_cases = [
        {"input": "abbaca", "expected": "ca"},
        {"input": "azxxzy", "expected": "ay"},
        {"input": "aaaaaaaa", "expected": ""},
        {"input": "abacaba", "expected": "abacaba"},
        {"input": "abcdef", "expected": "abcdef"},
    ]

    print("--- Running Remove All Adjacent Duplicates Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = remove_duplicates(test["input"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: Input='{test['input']}' | Result='{result}' | Expected='{test['expected']}' | {status}")

if __name__ == "__main__":
    run_tests()