# Two Pointers Pattern

A technique that involves using two integer variables (called pointers) to keep track of the indices while traversing a collection. Usually reduces time complexity from $O(N^2)$ to $O(N)$.

## Different Implementations

### **a) Converging Pointers (Outside-In)**

* Start pointers at the edge and move them towards each other.
* One pointer at the first element and the other pointer at the last element.
* **Visual Logic:** `[ L → . . . . . ← R ]`
* **See Example:** [Check If Palindrome](./EX_CheckifPalindrome.py)

### **b) Parallel Pointers (Two Iterables)**

* Start both pointers at the first index/element since we are dealing with two arrays or iterables.
* For this, you would need to check both arrays individually after the initial main while loop so we go through all the elements.
* **Think of it like 3 while loops:**
1. The **first** is where we move our pointers and stop until one of them reaches the end.
2. The **second and third** are to ensure exhaustive checks on both iterables separately.


* **See Example:** [Merge Sorted Arrays](./EX_mergedSortedArrays.py)

---

## When to use?

* When we have a **sorted array**.
* Any **palindrome problems**.

---

## List of Example Problems

* [EX_CheckifPalindrome.py](./EX_CheckifPalindrome.py) — *Basic converging pointers logic.*
* [EX_CheckForTarget.py](./EX_CheckForTarget.py) — *Finding a target sum in a sorted array.*
* [EX_isSubsequence.py](./EX_isSubsequence.py) — *Using parallel pointers to validate strings.*
* [EX_mergedSortedArrays.py](./EX_mergedSortedArrays.py) — *The 3-while-loop merge pattern.*

## List of Problems for Testing/Checking

* [reverseString.py](./reverse_string.py) - https://leetcode.com/problems/reverse-string/description/
* [sortedSquares.py](./sortedSquares.py) - https://leetcode.com/problems/squares-of-a-sorted-array/description/

---