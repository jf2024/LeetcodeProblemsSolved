from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list using the iterative three-pointer approach.
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next # first, make sure we don't lose the next node
        curr.next = prev      # reverse the direction of the pointer
        prev = curr           # set the current node to prev for the next node
        curr = next_node      # move on

        
    return prev

# A -----> B -------> C 

# At the start
# think of the arrows as "curr.next"

#NULL ------>   A   -----> B      -------> C 
#prev          curr.    next_node

#then when we do curr.next = prev it becomes this, we switch the curr pointer to null
#NULL <------   A   -----> B      -------> C 
#prev          curr.    next_node

#and after curr = next_node, it looks like this where we move the prev to curr and curr to next_node
# NULL <------   A   -----> B      -------> C 
#                prev.      curr.         next_node
# repeat process  




def build_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Helper to convert a Python list into a Linked List."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Helper to convert a Linked List back into a Python list for easy comparison."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], [])
    ]
    
    for i, (input_arr, expected) in enumerate(test_cases, 1):
        head = build_linked_list(input_arr)
        reversed_head = reverse_list(head)
        result = linked_list_to_list(reversed_head)
        
        passed = result == expected
        print(f"Test {i}: Input {input_arr} -> Expected {expected}, Got {result} | {'PASSED' if passed else 'FAILED'}")

if __name__ == "__main__":
    run_tests()