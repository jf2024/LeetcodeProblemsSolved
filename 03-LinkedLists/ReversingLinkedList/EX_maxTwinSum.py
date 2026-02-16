from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pair_sum(head: Optional[ListNode]) -> int:
    """
    Calculates the maximum twin sum of a linked list.
    Twins are defined as nodes at index i and (n-1-i).

    Time: O(N)
    Space: O(1)

    Practice Problem from the "Reversing Linkedlist Section" 
    """
    slow = head
    fast = head
    prev = None

    # 1) find the middle of our linkedlist 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2) reverse the second half of this list 
    # 'slow' is the start of the second half
    # could also create another variable to help with names
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # 3) we know that prev is the head of our reversed list
    # so we can just move head and prev at the same time to get our answer
    max_ans = 0
    while prev:
        curr_sum = prev.val + head.val
        max_ans = max(max_ans, curr_sum)

        prev = prev.next
        head = head.next

    return max_ans

# --- Helper Functions for Testing ---

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def run_test_cases():
    test_cases = [
        {"input": [5, 4, 2, 1], "expected": 6},   # (5+1), (4+2)
        {"input": [4, 2, 2, 3], "expected": 7},   # (4+3), (2+2)
        {"input": [1, 100000], "expected": 100001},
        {"input": [1, 2, 3, 4, 5, 6], "expected": 7} # (1+6), (2+5), (3+4)
    ]

    print("--- Running Twin Sum Tests ---")
    for i, test in enumerate(test_cases, 1):
        head = list_to_linked_list(test["input"])
        result = pair_sum(head)
        passed = result == test["expected"]
        print(f"Test {i}: Input {test['input']} | Expected {test['expected']} | Got {result} | Passed: {passed}")

if __name__ == "__main__":
    run_test_cases()