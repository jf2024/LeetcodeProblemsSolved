# 03-Linked Lists

# Core Concepts & Mechanics

## A. What is a Node?

A **Node** is the building block of a Linked List. It is a "container" that holds both data and a reference to where the next piece of data lives.

* **Data:** The value stored (integer, string, etc.).
* **Next:** A pointer to the next Node object.

---

## B. Linked Lists vs. Arrays

| Feature | Array | Linked List |
| --- | --- | --- |
| **Access** |  (Random Access) |  (Must traverse) |
| **Insert/Delete** |  (Requires shifting) |  (With reference) |
| **Memory** | Contiguous block | Scattered (Pointers) |

> **Why use Linked Lists?** They excel at dynamic size and  insertions/deletions at the ends or middle (if you already have the pointer). They don't require a large contiguous block of memory, which is helpful for fragmented systems.

---

## C. Traversal Mechanics

### 1. Moving vs. Modifying (The Golden Rule)

There is a vital distinction between moving your "view" and modifying the list's "skeleton."

* **Walking:** `curr = curr.next` moves your "feet" to a new node. You are just looking at a different object.
* **Surgery (Snipping):** `curr.next = curr.next.next` changes the "track" itself. This physically alters the list in memory.

**The Deletion Rule:**
When deleting nodes in a loop, only **Walk** (`curr = curr.next`) if you **didn't** perform **Surgery**. 
If you snipped a node, "stay put"—the new node that moved into the `.next` position needs to be checked immediately.

---

## D. Advanced Patterns: The "Anchor & Worker"

When building or modifying a list where the **Head** might change, we use two separate variables:

### 1. The Sentinel Node (The "Anchor")

A physical `ListNode(0)` created as a permanent placeholder at the start.

* **The Purpose:** It acts as a "fixed post" in the ground. You don't have to write `if head is None` logic because the Sentinel is **never** None.
* **The Return:** You always return `dummy.next` to get the real list.

### 2. The Traversal Pointer (The "Worker")

A variable (usually `curr`) that starts at the Anchor but walks down the list.

* **The Purpose:** The Worker hitches new nodes to the chain and then moves forward to the new end.
* **Why both?** If you moved the Sentinel variable itself, you would lose the start of your list.

---

### 3. Example: Merge Two Sorted Lists

This problem demonstrates how the **Anchor** stays put while the **Worker** builds the new list.
link to problem: https://leetcode.com/problems/merge-two-sorted-lists/description/

```python
def mergeTwoLists(list1, list2):
    # THE ANCHOR: Stays at the station so we can find the head later
    dummy = ListNode(0) 

    # THE WORKER: Starts at the anchor, moves forward to perform surgery
    curr = dummy 

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1   # SURGERY: Worker hitches list1 to the chain
            list1 = list1.next  # WALKING: list1 scout moves forward
        else:
            curr.next = list2   # SURGERY: Worker hitches list2 to the chain
            list2 = list2.next  # WALKING: list2 scout moves forward
        
        curr = curr.next        # WALKING: Worker moves to the new end of the chain

    # THE CLEANUP: Attach whichever list still has nodes left
    curr.next = list1 or list2

    # Return the node immediately after the Anchor
    return dummy.next
```

---

## E. Types of Linked Lists

1. **Singly Linked List:** Nodes point only to the **next** node (Forward only).
2. **Doubly Linked List:** Nodes point to both **next** and **previous** (Bidirectional).

---

# Algorthims/Techniques

## 1) Fast and Slow Pointers (Two-Pointer Technique)

The Two-Pointer technique in Linked Lists is an adaptation of the same strategy used for strings and arrays. The core idea is that the pointers do not move side-by-side; they move at different **speeds** or maintain a specific **distance**.

### A. Different Speeds 

The "fast" pointer moves through the list quicker than the "slow" pointer. This is primarily used for finding the middle of a list or detecting cycles.

* **Fast Pointer:** Moves **two** nodes per iteration (`fast = fast.next.next`).
* **Slow Pointer:** Moves **one** node per iteration (`slow = slow.next`).

> **⚠️ Vital Condition:** When moving two steps at a time, you **must** check both `fast` and `fast.next` in your loop to avoid a `NoneType` error.

**Pseudocode:**

```python
def fast_slow_speed(head):
    slow = head
    fast = head

    # Check both to ensure fast.next.next is valid
    while fast and fast.next:
        # Process logic here
        slow = slow.next
        fast = fast.next.next
    
    return slow # In many cases, slow is now at the middle
```

### B. Different Starting Positions (The "Gap" Strategy)

Instead of different speeds, both pointers move at **one node per iteration**, but the "fast" pointer is given a head start.

* Used for: Finding the -th node from the end.
* **Mechanic:** Move `fast`  steps ahead first, then start moving `slow`. When `fast` reaches the end (`None`), `slow` will be exactly  nodes from the end.

**Pseudocode:**

```python
def fast_slow_gap(head, k):
    slow = head
    fast = head

    # 1. Create the gap
    for _ in range(k):
        fast = fast.next
    
    # 2. Move together at the same speed
    # Only need to check 'fast' because we move 1 step at a time
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow
```

## 2) Linked List Deletion (Look-Ahead Pattern)
When removing nodes (like duplicates), you often only need one pointer. Instead of moving two pointers, you stand on `curr` and "look ahead" at `curr.next`.

* **Logic:** 1. If `curr.val == curr.next.val`, snip the duplicate: `curr.next = curr.next.next`.
    2. **Crucially**, do not move `curr` yet. The "new" `curr.next` might also be a duplicate.
    3. Only move `curr = curr.next` when the values are different.

**Pseudocode:**
```python
while curr and curr.next:
    if curr.val == curr.next.val:
        curr.next = curr.next.next  # Snip the duplicate
    else:
        curr = curr.next            # Move to next unique node
```


#### Example Problems:

* [Find Middle](./Fast&SlowPointers/EX_findMiddle.py) 
* [Has Cycle](./Fast&SlowPointers/EX_hasCycle.py)
* [Find Kth Node](./Fast&SlowPointers/EX_findKthNode.py)
    - good example of the gap strategy

#### Testing Problems: 
* [Delete Duplicates](./Fast&SlowPointers/deleteDuplicates.py)
    - good problem to review
---

## 3) Reversing a Linked List

### The Three-Pointer Strategy

We use three pointers to ensure we never lose our place in memory:

1. **`prev`**: The node we just finished reversing (our new "next").
2. **`curr`**: The node we are currently flipping.
3. **`next_node`**: Our "Scout" that holds onto the rest of the list (temp variable).

### Code Implementation

```python
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # 1. SCOUT (Save the future)
        curr.next = prev       # 2. SURGERY (Flip the pointer)
        prev = curr            # 3. STEP (Move prev forward)
        curr = next_node       # 4. STEP (Move curr forward)
        
    return prev
```

### Step-by-Step: The First Iteration

Imagine our list is: `A -> B -> C -> NULL`

**Initial State:**

* `prev` = `None`
* `curr` = `A`

| Action | Code | Resulting State |
| --- | --- | --- |
| **1. Scout** | `next_node = curr.next` | `next_node` is now pointing at **B**. (We won't lose the rest of the list!) |
| **2. Surgery** | `curr.next = prev` | **A** now points to `None`. The bond between A and B is broken. |
| **3. Step** | `prev = curr` | `prev` label moves to **A**. |
| **4. Step** | `curr = next_node` | `curr` label moves to **B**. |

**End of Iteration 1:**
`None <- A(prev)` ... `B(curr) -> C -> NULL`

And immediatly after, next_node = curr.next, C would be the next_node 

---

### Why we return `prev`

By the time the `while` loop finishes, `curr` has walked off the edge of the list and is `None`. `prev`, however, is standing on the **very last node** we processed—which is now the **new head** of the reversed list.

---

### Example Problems:
* [Reverse LinkedList](./ReversingLinkedList/EX_reverseList.py)
* [Swap Nodes in Pairs](./ReversingLinkedList/EX_swapPairs.py) - https://leetcode.com/problems/swap-nodes-in-pairs/
* [Maximum Twin Sum of a Linked List](./ReversingLinkedList/EX_maxTwinSum.py) - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

* NOTE: ALL GOOD PROBLEMS TO REVIEW AND LOOK BACK ON, ESPECIALLY SWAP NODES AND TWINSUM
