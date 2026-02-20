def is_valid(s: str) -> bool:
    """
    Time: O(N)
        - n is the size of the input array


    Space: O(N)
        - stack's size grow linearly with the input size
    """

    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}

    for current_opening_bracket in s:
        if current_opening_bracket in matching: 
            stack.append(current_opening_bracket)

        else:
            if not stack: #if our stack is empty and we have a closing bracket to start
                return False 
            
            most_recent_opening = stack.pop()
            closing_bracket = matching[most_recent_opening]
            if closing_bracket != current_opening_bracket:
                return False
            
    return not stack   #if our stack is empty, return True since we matched all of our brackets


def run_tests():
    test_cases = [
        {"input": "()", "expected": True},
        {"input": "()[]{}", "expected": True},
        {"input": "(]", "expected": False},
        {"input": "([])", "expected": True},
        {"input": "([)]", "expected": False},
        {"input": "{[]}", "expected": True},
        {"input": "]", "expected": False},
    ]

    print("--- Running Valid Parentheses Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = is_valid(test["input"])
        passed = result == test["expected"]
        print(f"Test {i}: Input='{test['input']}' | Expected={test['expected']} | Result={result} | Passed: {passed}")

if __name__ == "__main__":
    run_tests()