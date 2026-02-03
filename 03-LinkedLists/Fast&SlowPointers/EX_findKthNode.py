class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getKthFromEnd(head: ListNode, k: int) -> ListNode:
    """
    Given the head of a linked list and an integer k, 
    return the kth node from the end.
    
    Constraint: k is guaranteed to be less than or equal to 
    the number of nodes in the list.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next

    return slow



# Helper to build list
def build_ll(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

if __name__ == "__main__":
    # Test Case: 1 -> 2 -> 3 -> 4 -> 5, k = 2
    ll = build_ll([1, 2, 3, 4, 5])
    result = getKthFromEnd(ll, 2)
    print(f"2nd from end value: {result.val if result else 'None'}") # Expected: 4