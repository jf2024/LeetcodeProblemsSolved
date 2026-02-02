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

## 1) Fast Pointer

write here later

## 2) Slow Pointer
write here later




---