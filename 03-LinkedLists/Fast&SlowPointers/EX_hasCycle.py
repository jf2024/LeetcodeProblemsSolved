class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    """
    Given the head of a linked list, determine if it has a cycle.
    Return True if a cycle exists, False otherwise.

    Time Complexity: O(N) = number of nodes in a linkedlist
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

"""
You can also use hashing for this (think if we need a set or dictionary)
Might be a fun execrise to try

However with the hasing solution, we would be using O(N) space instead of O(1) space used in linkedlist
"""

# Helper to create a cycle for testing
def create_cycle_list():
    # 3 -> 2 -> 0 -> -4
    #      ^          |
    #      |__________|


    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle back to node2
    
    return node1

if __name__ == "__main__":
    # Test Case 1: Has Cycle
    ll_cycle = create_cycle_list()
    print(f"Test 1 (Has Cycle): {hasCycle(ll_cycle)}") # Expected: True

    # Test Case 2: No Cycle
    ll_no_cycle = ListNode(1, ListNode(2))
    print(f"Test 2 (No Cycle): {hasCycle(ll_no_cycle)}") # Expected: False