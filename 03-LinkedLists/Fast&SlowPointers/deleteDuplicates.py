from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates_TwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Version 1: Two Pointers (Slow and Fast) 

        MY ORIGINAL IMPLEMENTATION
        
        Logic: Use 'slow' to track the current unique node and 'fast' to inspect
        the next candidate. If they match, 'slow' stays put and snips the 
        duplicate out of the chain.
        
        Complexity:
            Time: O(N) - Each node is visited once.
            Space: O(1) - Only two pointers used.
        """


        if not head:
            return None
            
        slow = head
        fast = head.next
        
        while fast:
            if slow.val == fast.val: #found a duplicate, but we dont move slow yet, just changing the pointer
                slow.next = slow.next.next
                # Fast moves to the next node to check it.
                fast = fast.next    #move fast for next check/iteration
            else:
                # No match. Move both forward.
                slow = slow.next
                fast = fast.next
                
        return head

    def deleteDuplicates_OnePointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Version 2: Single Pointer (Look-Ahead)
        
        Logic: Instead of a second variable, we just look at curr.next. 
        If curr and curr.next have the same value, we bypass curr.next.
        
        Complexity:
            Time: O(N)
            Space: O(1)
        """
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Stay on 'curr', but change its 'next' pointer
                curr.next = curr.next.next
            else:
                # Only walk forward when the current value is unique
                curr = curr.next
                
        return head

# Helper to print the list
def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Empty")

if __name__ == "__main__":
    sol = Solution()
    
    # Test: 1 -> 1 -> 2 -> 3 -> 3
    test = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print("Original List:")
    print_list(test)
    
    result = sol.deleteDuplicates_OnePointer(test)
    print("\nAfter Deleting Duplicates:")
    print_list(result)