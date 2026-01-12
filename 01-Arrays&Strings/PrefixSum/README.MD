# Prefix Sum Pattern

A technique used primarily on arrays of numbers where we pre-calculate a "prefix array." Each element at index $i$ in the prefix array represents the sum of all elements from the beginning of the input up to $j$. This allows us to calculate the sum of any contiguous subarray in $O(1)$ time.

## Implementations

We always need to build this prefix sum array as the **first step**. After we build this array, we then need to do one of the following: either **Range Sum Queries** or **Splitting Arrays**.

### **1. Building the Prefix Sum**

The most common way to build it is to initialize the prefix array with the first element and then iterate through the rest:

```python
prefix = [nums[0]]
for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])
```

### **2. Choice A: Range Sum Queries ( Sums)**

To find the sum of a subarray from index `i` to `j`:

* **Formula:** `sum = prefix[j] - prefix[i] + nums[i]`
* **Why?** `prefix[j]` contains the sum from index `0` to `j`. `prefix[i]` contains the sum from `0` to `i`. By subtracting them, you remove everything before `i`. We add `nums[i]` back because the subtraction removes it.
* **Alternative:** There is an alternative version that uses a prefix array that is len(nums) + 1 in length, starting with a 0. This makes the formula simpler: prefix[j + 1] - prefix[i]. 
* **Note** However for my purposes and to keep this simple, I will just stick with the original formula as described above


### **3. Choice B: Splitting Arrays**

In "Split" problems (like [waysToSplitArray.py](https://www.google.com/search?q=./EX_waysToSplitArray.py)), you don't usually need the complex range formula. You just need to know:

* **Left Part Sum:** `prefix[i]`
* **Right Part Sum:** `prefix[-1] - prefix[i]` (Total sum minus the left sum).

---

## When to Use?

* **Sum Queries:** When you need to find the sum of many different contiguous subarrays (Range Sum Queries).
* **Array Splitting:** When you need to find a pivot point where the left side and right side meet a certain condition.
* **Reducing $O(N^2)$ to $O(N)$ to :** If you find yourself using a nested loop just to calculate sums, Prefix Sum is likely the solution.

---

## Key Formulas

| Goal | Formula |
| --- | --- |
| **Sum of subarray [i, j]** | `prefix[j] - prefix[i] + nums[i]` |
| **Sum of the "Right" side** | `prefix[-1] - prefix[i]` |

---

## List of Example Problems

* [EX_answerQueries.py](./EX_answerQueries.py) — *Standard Range Sum Query usage.*
* [EX_waysToSplitArray.py](./EX_waysToSplitArray.py) — *Using prefix sum to compare array splits in .*

## List of Problems for Testing/Checking

* [runningSum1dArray.py](./runningSum1dArray.py) - https://leetcode.com/problems/running-sum-of-1d-array/
* [minValuePostiveStepSum.py](./minValuePostiveStepSum.py) - https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
* [kRadiusSubArrayAvg.py](./kRadiusSubArrayAvg.py) - https://leetcode.com/problems/k-radius-subarray-averages/description/

---