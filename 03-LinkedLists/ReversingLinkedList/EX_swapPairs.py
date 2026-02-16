from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a linked list, swap every two adjacent nodes 
    and return its head. You must solve the problem without 
    modifying the values in the list's nodes (i.e., only nodes 
    themselves may be changed).
    """
    dummy = ListNode(0) #creating our "null" so our first node points to nothing
    dummy.next = head   #what we will return, don't rlly need this line but good to have just to see

    prev = dummy    #will point to our dummy or placeholder for now 
    curr = head     #entering our list to traveres, first node of first pair

    # for the even case, curr will be none and loop breaks
    # for the odd case, curr.next will be none and loop breaks
    while curr and curr.next: 
        #save pointers (our pairs)
        nxtPair = curr.next.next #first node of next pair

        #second node of our pair
        second = curr.next 

        #reverse this pair
        second.next = curr  #second node pointer will point to the first node
        curr.next = nxtPair #first node pointer will point to the first node of the next pair
        prev.next = second  #previous pointer will point to the second node of pair, for the first loop/iteration, second node
        #will be the be new head which makes sense for prev.next to point at it

        #update pointers for next two nodes
        prev = curr     #move our prev which was at dummy, and make it to curr 
        curr = nxtPair  #set curr to the first node of our next pairs so we can reverse for the next iteration

    return dummy.next


# Helper to build and print
def build_ll(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def print_ll(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    test_list = build_ll([1, 2, 3, 4, 5, 6])
    print("Original:")
    print_ll(test_list)
    
    swapped = swapPairs(test_list)
    print("Swapped:")
    print_ll(swapped) # Expected: 2 -> 1 -> 4 -> 3 -> 6 -> 5