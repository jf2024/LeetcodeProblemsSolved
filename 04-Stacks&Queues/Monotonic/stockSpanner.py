class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span

# --- Test Cases ---
def run_tests():
    spanner = StockSpanner()
    
    # Test inputs and expected outputs
    calls = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    
    print("--- Running Stock Spanner Tests ---")
    results = []
    for price in calls:
        results.append(spanner.next(price))
        
    passed = results == expected
    print(f"Input prices: {calls}")
    print(f"Result:       {results}")
    print(f"Expected:     {expected}")
    print(f"Status:       {'PASSED' if passed else 'FAILED'}")

    # Additional Test Case
    print("\n--- Running Custom Test Case ---")
    spanner2 = StockSpanner()
    # [7, 2, 1, 2] today is 2 -> span 4
    custom_prices = [7, 2, 1, 2, 2]
    custom_expected = [1, 1, 1, 2, 3] # 7(1), 2(1), 1(1), 2(3 days: 2,1,2), 2(4 days: 2,2,1,2)
    
    custom_results = [spanner2.next(p) for p in custom_prices]
    print(f"Prices:   {custom_prices}")
    print(f"Results:  {custom_results}")

if __name__ == "__main__":
    run_tests()