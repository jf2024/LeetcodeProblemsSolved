# 03-Linked Lists

# Core Concepts & Mechanics

## A. What is a Node?

A **Node** is an object that acts as the building block of a Linked List. Unlike a simple array element, a Node is a "container" that holds both data and pointers to other nodes.

* **Data:** The value stored (integer, string, etc.).
* **Next:** A reference (pointer) to the next Node in the sequence.

---

## B. Linked Lists vs. Arrays

| Feature | Array | Linked List |
| --- | --- | --- |
| **Access** |  (Random Access) |  (Must traverse) |
| **Insert/Delete** |  (Requires shifting) |  (With reference) |
| **Memory** | Contiguous block | Scattered (Pointers) |
| **Size** | Fixed (or costly to resize) | Dynamic (Grows easily) |

> **Note on Space:** While both have O(N) space complexity, Linked Lists have more **overhead** because they must store the pointer (`.next`) in addition to the data.

> **Why use Linkedlist over Arrays?** For insertation/deletion at the ends or middlle (provided we have a pointer). With an array, inserting at index O is O(N) because every element must shift. With a linkedlist, we just change two pointers. In addition, linkedlist don't require a *contiguous block of memory*. 

---

## C. Mechanics & Traversal

### 1. Pointer Assignment

Assigning a pointer refers to an object in memory. Variables remain at nodes unless modified directly.

* `ptr = head`: `ptr` now looks at the same object as `head`.
* `head = head.next`: `head` moves forward to the next node.

### 2. Chaining

We connect nodes by setting the `.next` property.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two   # 1 -> 2
two.next = three # 1 -> 2 -> 3
head = one

```

### 3. Traversal

Since we don't have indices, we use a `while` loop. The loop terminates when we hit `None` (the end of the list) or in other words, when head is None/Null.

```python
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next # Move to the next "link" in the chain
    return ans

```

### 4. Walking the Track vs. Changing the Track
Recall the traversal section on how we moved along in a linkedlist, there is a vital distinguish between moving your variable and modifying the list's structure.

* **Walking:** `curr = curr.next` moves your "feet" to a new node. You are changing which node we are looking at (basically the traversal from above)
* **Changing (Snipping):** `curr.next = curr.next.next` changes the "track" itself. (but not actually moving along)

**The Golden Rule of Deletion:**

When deleting nodes in a loop, only move your **"feet"(walking)** (`curr = curr.next`) if you **didn't** delete anything. 

If you did delete a node (**snipping**), stay put—the new node that shifted into the `.next` position needs to be checked next.

---

## D. Types of Linked Lists

1. **Singly Linked List:** Each node points only to the **next** node. (Forward only).
2. **Doubly Linked List:** Each node points to both the **next** and the **previous** node. (Bidirectional).

---

## E. Sentinel Nodes

**Sentinel nodes** (also called "Dummy" nodes) are extra nodes placed at the start (`head`) and end (`tail`) of a list that **do not contain real data.**

* **Why use them?** They eliminate edge cases. For example, deleting a node usually requires checking if `node.prev` or `node.next` is null. With Sentinels, every "real" node always has a neighbor.
* **Structure:** * `Sentinel Head -> Real Node 1 -> Real Node 2 -> Sentinel Tail`
* The "real" head is always `sentinel_head.next`.

---

## F. Dummy Pointers

A **Dummy Pointer** is simply a temporary variable used to traverse the list so you don't lose the reference to the original `head`. If you move the `head` variable itself during a calculation, you can never get back to the start of the list!

```python
def get_sum(head):
    ans = 0
    curr = head # 'curr' is our dummy pointer
    while curr:
        ans += curr.val
        curr = curr.next
    
    # We can still access the start of the list using 'head'
    return ans

```

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
