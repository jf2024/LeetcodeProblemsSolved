from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:

        while self.queue and len(self.queue) >= self.size:
            self.queue.popleft()

        self.queue.append(val)

        return sum(self.queue) / len(self.queue)

# --- Test Cases ---
def test_moving_average():
    print("--- Running Moving Average Tests ---")
    
    # Initialize with window size 3
    ma = MovingAverage(3)
    
    results = []
    results.append(ma.next(1))   # Expected: 1.0
    results.append(ma.next(10))  # Expected: 5.5
    results.append(ma.next(3))   # Expected: 4.66667
    results.append(ma.next(5))   # Expected: 6.0
    
    expected = [1.0, 5.5, 4.66667, 6.0]
    
    for i, (res, exp) in enumerate(zip(results, expected)):
        passed = abs(res - exp) < 1e-5
        print(f"Call {i+1}: Result={res:.5f} | Expected={exp:.5f} | Passed: {passed}")

if __name__ == "__main__":
    test_moving_average()