def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Time: O(N)

    Space: O(N)
    """

    stack = []
    ans = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_day_index = stack.pop()
            days_waited = i - prev_day_index #i is our current_day 
            ans[prev_day_index] = days_waited

        stack.append(i)

    return ans

def run_tests():
    test_cases = [
        {
            "input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0]
        },
        {
            "input": [30, 40, 50, 60],
            "expected": [1, 1, 1, 0]
        },
        {
            "input": [30, 60, 90],
            "expected": [1, 1, 0]
        },
        {
            "input": [80, 80, 80],
            "expected": [0, 0, 0]
        }
    ]

    print("--- Running Daily Temperatures Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = daily_temperatures(test["input"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: Input={test['input']}")
        print(f"Result:   {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status:   {status}\n")

if __name__ == "__main__":
    run_tests()