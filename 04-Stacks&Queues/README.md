# 04 - Stacks & Queues

# Stacks

## Core Concepts

* **Definition**: Ordered collection of elements where you can only add or remove elements from the same end.
    * Think of a stack of plates, where you can add or remove from the top of the pile.
    * Also known as **LIFO --> Last In, First Out**.

* **Example**: `stack = [a, b, c]`
    * To add is called **push**.
    * To remove is called **pop**.
    * Can also **peek**, looking at the element at the top of the stack without removal.
    * So if we wanted to pop from our stack, we would have `[a, b]`.
    * If we wanted to push "d" to our stack, it would now be `[a, b, d]`.

* Can implement using a dynamic array or LinkedList.
    * Usually **$O(1)$** for push, pop, random access.
    * **$O(N)$** for search.


* **Key phrases on when to use stack** (sometimes hard to spot):
    * Matching elements together.
    * Querying some property "how far is the next largest element."
    * Evaluate mathematical equation as a string.



### Example Problems

* [Valid Parentheses](./Stacks/EX_validParentheses.py)
* [Remove All Adjacent Duplicates in String](./Stacks/EX_removeAdjacentDuplicates.py)
* [Backspace String Compare](./Stacks/EX_BackspaceCompare.py)
    * Can also use two pointers to solve this problem.

### Testing Problems

* [Simplify Path](./Stacks/simpliftPath.py)
    * Good problem to review.
* [Make the String Great](./Stacks/makeGoodStrings.py)

---

# Queues

## Core Concepts

* **FIFO**: **First In, First Out**.
    * Think of a line at a restaurant; the first person orders their food and is the first one to leave the line.
    * In stacks, elements are added and removed from one side. With **queues**, elements are added from one side and removed from the other side.
    * Add elements: **enqueue**.
    * Delete elements: **dequeue**.


* Can technically use dynamic arrays to implement a queue but will be **$O(N)$** when removing or adding from the front of the array.
    * *Remember*: Each element has a fixed address, so if we add or remove, we need to shift our elements which is $O(N)$ where $n$ is the size of the array.

* Instead, we can use **doubly linked lists** since we have pointers instead. With this, our addition or deletion becomes **$O(1)$**, so it's now much more efficient.
    * Moving forward, we will implement a **deque** (double-ended queue).
    * With a deque, we can add or remove elements from either side.
    * In a regular queue, usually add elements to one side and delete from the other side.

* `from collections import deque`

* Less common problems than stacks, as queues are usually for **BFS (Breadth-First Search)**, but outside of that, not really used standalone like the previous data structures.

### Example and Testing Problems

* [Recent Counter](./Queues/EX_recentCounter.py)
* [Moving Average](./Queues/movingAverage.py)

---

# Monotonic

## Core Concepts

* **Definition**: The elements are always sorted either in increasing or decreasing order.
    * **Ex**: `stack = [1, 5, 8, 15, 23]`
    * If we wanted to add 14, we would need to pop 15 and 23 first before pushing 14.


### Pseudocode

```python
stack = []
for num in nums: # or using range(len)
    while stack and stack[-1] >= num:
        stack.pop()
    # some logic depending on problem
    stack.push(num)

```

* **Useful for**:
    * Finding the next element based on some criteria (Next Greater Element).
    * For dynamic window of elements and wanting to maintain the max or min element when our window changes.


### Example Problems (All good examples to review)

* [Daily Temperatures](./Monotonic/EX_dailyTemperatures.py)
* [Sliding Window Maximum](./Monotonic/EX_slidingWindowMax.py)
* [Longest Subarray Difference](./Monotonic/EX_longestSubarrayAbsDiff.py)

### Testing Problems
* [Next Greater Element](./Monotonic/nextGreaterElement.py) - https://leetcode.com/problems/next-greater-element-i/description/
* [Online Stock Span](./Monotonic/stockSpanner.py)

## Metadata Bundling in Stacks (Online Stock Span Notes)

### The Concept

Sometimes, a raw value (like a price) isn't enough to solve the problem efficiently. You need to "bundle" the value with metadata—extra information that describes the state of that value. [airtribe](https://www.airtribe.live/dsa-sheet/resource/online-stock-span)

### Why use it?

It allows the stack to "remember" work that was already completed. Instead of re-calculating history, you "collapse" previous results and store them in a tuple or list. [thita](https://thita.ai/blog/dsa/stack-patterns)

### The "Handover" Pattern

When a new element pops an old one, it "inherits" the old element's metadata. [airtribe](https://www.airtribe.live/dsa-sheet/resource/online-stock-span)

Example: In Stock Spanner, the span is the metadata. When a higher price pops a lower one, it adds the lower one's span to its own. [airtribe](https://www.airtribe.live/dsa-sheet/resource/online-stock-span)

***

### Common Bundle Patterns

- `(value, count/span)`: Used to skip over already-processed consecutive elements.
- `(value, current_min)`: Used in "Min Stack" problems to track the minimum in O(1).
- `(value, index)`: Used when you need to calculate distances or widths (like in histograms).

**Pro-Tip:** If you find yourself thinking, "I wish I didn't have to re-count these elements," you probably need to bundle a count variable into your stack.

---

## Cheat Sheet: Sliding Window vs. Monotonic Window

| Feature | Standard Sliding Window | Monotonic Sliding Window |
| --- | --- | --- |
| **Main Goal** | Track a **total sum** or **count** of the window. | Track the **Max or Min** element of the window. |
| **Data Tool** | Two Pointers + a single Variable (sum/count). | Two Pointers + a **Deque**. |
| **When to use?** | When all elements contribute to a total (e.g., Sum < K). | When one "Leader" element dictates the window (e.g., Max - Min < K). |
| **Logic on "Left"** | Subtract `nums[left]` from the total. | Only pop from deque if `nums[left]` is the current Max/Min. |

# Testing LeetCode Problems to 


