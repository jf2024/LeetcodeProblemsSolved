class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head: ListNode) -> int:
    """
    Given the head of a linked list with an odd number of nodes,
    return the value of the node in the middle.

    Version 1 - Using a dummy pointer
    """
    length = 0
    dummy = head

    while dummy:
        length += 1
        dummy = dummy.next

    for _ in range(length // 2):
        head = head.next
    
    return head.val


def findMiddle(head: ListNode) -> int:
    """
    Given the head of a linked list with an odd number of nodes,
    return the value of the node in the middle.

    Version 2 - Using Fast and Slow Pointers
    """

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


"""
While both versions have the same
    - Time Complexity: O(N)
    - Space Complexity: O(1)

The second version looks at every node once while the first version looks at every node twice. So in practice the 
second version is more efficient 
"""
        


# Helper function to build a linked list from a list for testing
def build_ll(arr):
    if not arr: return None

    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return head

if __name__ == "__main__":
    # Test Case: 1 -> 2 -> 3 -> 4 -> 5
    ll1 = build_ll([1, 2, 3, 4, 5])
    print(f"Middle Value: {findMiddle(ll1)}") # Expected: 3