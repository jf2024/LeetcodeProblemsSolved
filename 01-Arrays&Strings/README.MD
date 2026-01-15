# Arrays and Strings

This section covers the core techniques used to solve Array and String problems, as explored in the Leetcode course.

## 1. Two Pointers

Used when we need to iterate through an array or string by tracking two different positions simultaneously.

* **Opposite Ends:** Pointers start at index `0` and `len(arr) - 1` and move toward each other. Used for reversing strings or checking palindromes.
* **Two Sequences:** One pointer for each array. Used for merging sorted arrays or checking for subsequences.
* **Time Complexity:** Usually  or  as each pointer only moves in one direction.

## 2. Sliding Window

A specific type of two-pointer technique used for **contiguous** segments (subarrays or substrings).

* **Fixed Window:** The window size is constant. We "slide" it by adding a new right element and removing the old left element.
* **Dynamic Window:** The window expands with the right pointer and shrinks with the left pointer whenever a constraint is broken.
* **Common Use:** Finding the maximum/minimum sum or length of a subarray that meets a specific condition.

## 3. Prefix Sum

A pre-computation technique where we create an array that stores the cumulative sum of elements.

* **The Logic:** `prefix[i]` stores the sum of all elements from index `0` to `i`.
* **Standard Formula:** Sum of subarray `[i, j] = prefix[j] - prefix[i] + nums[i]`
* **Use Case:** Great for problems involving multiple *range sum queries* or *array splitting* where you need to find sums in `O(1)` time.

---

## Other Notes to Consider

### a) String Building

* In Python, **strings are immutable**.
* Some problems require us to build a string and concatenate elements. If we add one element at a time to a string (`s += char`), Python must copy the entire string each time, resulting in $O(N^2)$ time.
* To build a string in `O(1)` time instead, we should append characters to a list and join them at the end:

```python
def build_string(s):
    arr = []
    for c in s: 
        arr.append(c)
    return "".join(arr)
```

### b) Subarrays vs. Subsequences vs. Subsets

#### 1. Subarrays / Substrings

* **Definition:** A **contiguous** section of an array or string.
* **Ask:** Generally asks about max/min length, the number of subarrays, or max/min sum.
* **Constraints:** Often involves sums greater/less than `k`, max `k` unique elements, or "no duplicates allowed."
* **Formula:** Recall that `right - left + 1` calculates both the **size** of the current window and the **number of subarrays** ending at that right pointer.

#### 2. Subsequences

* **Definition:** A set of elements that keeps the **same relative order** but does not need to be contiguous.
* **Example:** `[1, 2, 3, 4]` → Subsequences include `[1, 3]`, `[4]`, `[]`, `[2, 3]`.
* **Invalid:** `[3, 2]` (wrong order) or `[5]` (not in array).
* **Note:** Usually saved for Dynamic Programming, but we covered an example in the Two Pointers section (e.g., checking if one string is a subsequence of another).


#### 3. Subsets

* **Definition:** Any set of elements from an array or string; **order does not matter**.
* **Example:** `[1, 2, 3, 4]` → Subsets include `[1, 3]`, `[4]`, `[3, 2]`.
* **Note:** Usually `[1, 2, 4]` and `[4, 1, 2]` are considered the same subset, so we don't double-count.
* **Strategy:** If a problem involves subsequences but order doesn't matter, treat it like a subset. This means we can **sort** the array. If it is a true subsequence problem, we cannot sort because order matters.

---

## List of Testing Leetcode Problems

### Two Pointers



### Sliding Window


### Prefix Sum


---