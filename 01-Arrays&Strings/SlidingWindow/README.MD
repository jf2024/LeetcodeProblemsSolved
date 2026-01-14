# Sliding Window Pattern

A technique implemented using two pointers to track a **contiguous** segment of data. It is primarily used to optimize problems from $O(N^2)$ to $O(N)$ by avoiding redundant calculations within subarrays.

## Different Implementations

### **a) Dynamic Window (Variable Size)**

The most common approach uses a `for` loop to expand the window and a `while` loop to shrink it.

**The Logic:**

1. Iterate through the array with a **right** pointer (the `for` loop).
2. Add the current element to your window tracking (sum, frequency, etc.).
3. Use a `while` loop to check if the window is **invalid**.
4. Inside the `while` loop, move the **left** pointer to shrink the window until it becomes valid again.


### **b) Fixed Window Size**

Used when the problem specifies a window length  (e.g., "Find the largest sum of a subarray of length 5").

**The Logic:**

1. Use an initial `for` loop to build the very first window (from index `0` to `k-1`).
    - `for i in range(k) #first for loop` 
    - can also do a `sum(nums[:k])` instead of a for loop, either way works (add the first k numbers or up to element k but not including) 
2. Use a second `for` loop to iterate through the rest of the array.
    - `for i in range(k, len(nums))`
3. **Slide the window:** Add the new "right" element and subtract the "left" element that is falling out of the window.
    - `curr += nums[i] #right pointer` 
    - `curr -= nums[i - k] #left one`

* **Example:** `nums = [1, 2, 3, 4, 5]`, `k = 3`
* On the first slide, `right = 3`. The element to remove is `nums[3 - 3]` (index 0).


---

## When to Use?

* **Subarrays:** When the problem mentions a **contiguous** section of an array.
    * *Example:* For `[1, 2, 3, 4]`, valid subarrays are `[1, 2]` or `[2, 3, 4]`, but not `[1, 3]`.


* **Optimization Criteria:** Finding the **maximum/minimum length** of a subarray that fits a condition.
* Finding the **total number** of subarrays that fit a condition.
* Dealing with a **fixed window size** .

---

## Key Formulas

| Goal | Formula |
| --- | --- |
| **Find Length** | `ans = max(ans, right - left + 1)` |
| **Find Total Number** | `ans += right - left + 1` |

> **Note:** The value `right - left + 1` represents the current length of the window and the number of valid subarrays ending at the current `right` pointer.

---

## List of Example Problems

* [EX_findLengh.py](./EX_findLengh.py) — *Finding the longest subarray sum .*
* [EX_maxConsecutiveOnesII.py](./EX_maxConsecutiveOnesII.py) — *Longest substring of 1s with at most one flip.*
* [EX_subarrayProductLessThanK.py](./EX_subarrayProductLessThanK.py) — *Counting the number of valid subarrays using window length.*
* [EX_fixedWindowMaxSum.py](./EX_fixedWindowMaxSum.py) — *Basic fixed-size window implementation for maximum sum.*

## List of Problems for Testing/Checking

* [maxAverageSubarrayI.py](./maxAverageSubarrayI.py) — https://leetcode.com/problems/maximum-average-subarray-i/description/
* [maxConsecutiveOnesIII.py](./maxConsecutiveOnesIII.py) — https://leetcode.com/problems/max-consecutive-ones-iii/description/
