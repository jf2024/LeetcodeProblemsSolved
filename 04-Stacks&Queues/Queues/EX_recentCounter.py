from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)
    

def test_recent_counter():
    rc = RecentCounter()

    print("--- Test Set 1 ---")
    print(f"Result: {rc.ping(1)} | Expected: 1")      
    print(f"Result: {rc.ping(100)} | Expected: 2")    
    print(f"Result: {rc.ping(3001)} | Expected: 3")   
    # 3002 - 3000 = 2. Since 1 < 2, 1 is removed.
    print(f"Result: {rc.ping(3002)} | Expected: 3")   

    print("\n--- Test Set 2: Boundaries ---")
    rc2 = RecentCounter()
    print(f"Result: {rc2.ping(3000)} | Expected: 1")  
    # 6000 - 3000 = 3000. 3000 is NOT < 3000, so it stays.
    print(f"Result: {rc2.ping(6000)} | Expected: 2")  
    # 6001 - 3000 = 3001. 3000 is < 3001, so it is popped.
    print(f"Result: {rc2.ping(6001)} | Expected: 2")  

    print("\n--- Test Set 3: Tightly Packed ---")
    rc3 = RecentCounter()
    times = [100, 200, 300, 3100, 3200, 7000]
    expected = [1, 2, 3, 4, 4, 1]
    for t, exp in zip(times, expected):
        print(f"Time: {t} | Result: {rc3.ping(t)} | Expected: {exp}")

if __name__ == "__main__":
    test_recent_counter()