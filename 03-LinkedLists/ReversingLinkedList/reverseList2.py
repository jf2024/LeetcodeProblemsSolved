from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse the nodes of the list from position left to position right.

    TIME: O(N)

    SPACE: O(1)

    needed some help from gemini to get to this answer

    Summaries of some key variables below:
        - left_prev = L - 1  (the left - 1 node before curr to attach its next pointer to prev later)
        - prev = ends at R  (new head after reversal)
        - new_tail = stays at L (new tail after reversal)
        - curr = ends at R + 1 (remainder of the list)
    """

    #create our dummy node just in case our first node (head) changes
    #if we dont, then we would need a bunch of if/else logic and this just simplifies that
    dummy = ListNode(0)
    dummy.next = head

    #set our left previous to dummy and curr to head like normal
    left_prev = dummy
    curr = head

    #find the "left - 1" node 
    count = 0
    while count != left - 1:    #can also just use a for loop and range(left - 1)
        left_prev = curr    #update our left_prev which is 1 behind curr 
        curr = curr.next
        count += 1


    # need to save our new_tail, which will be current
    # think about it, after we reverse our list, our curr node will be the tail 
    new_tail = curr 

    # normal reverse linkedlist code
    prev = None 
    for _ in range(right - left + 1): #right - left + 1 --> how many steps/items between index i and j
        next_node = curr.next
        curr.next = prev
        prev = curr 
        curr = next_node

    left_prev.next = prev #attach left - 1 node to prev, remember that prev becomes our new head 
    new_tail.next = curr  #attach our new tail pointer to the rest of the list which is just curr

    return dummy.next


# --- Helper Functions for Testing ---

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def run_tests():
    test_cases = [
        {
            "head": [1, 2, 3, 4, 5],
            "left": 2,
            "right": 4,
            "expected": [1, 4, 3, 2, 5]
        },
        {
            "head": [5],
            "left": 1,
            "right": 1,
            "expected": [5]
        },
        {
            "head": [3, 5],
            "left": 1,
            "right": 2,
            "expected": [5, 3]
        }
    ]

    print("--- Running Reverse Linked List II Tests ---")
    for i, test in enumerate(test_cases, 1):
        head = list_to_linked_list(test["head"])
        result_node = reverseBetween(head, test["left"], test["right"])
        result_list = linked_list_to_list(result_node)
        
        passed = result_list == test["expected"]
        print(f"Test {i}: Left={test['left']}, Right={test['right']}")
        print(f"   Input:    {test['head']}")
        print(f"   Expected: {test['expected']}")
        print(f"   Got:      {result_list}")
        print(f"   Passed:   {passed}\n")

if __name__ == "__main__":
    run_tests()