def backspace_compare(s: str, t: str) -> bool:
    """
    MY ORIGINAL IMPLEMENTATION

    TIME: O(N + M)
        - iterate through s (O(N))
        - iterate through t (O(M))

    SPACE: O(N + M)
        - store all s characters (O(N))
        - store all t characters (O(M))
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