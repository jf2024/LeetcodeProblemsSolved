# Arrays and Strings

This section covers the core techniques used to solve Array and String problems, as explored in the Leetcode course.

## 1. Two Pointers

Used when we need to iterate through an array or string by tracking two different positions simultaneously.

* **Opposite Ends:** Pointers start at index `0` and `len(arr) - 1` and move toward each other. Used for reversing strings or checking palindromes.
* **Two Sequences:** One pointer for each array. Used for merging sorted arrays or checking for subsequences.
* **Time Complexity:** Usually  or  as each pointer only moves in one direction.

## 2. Sliding Window

A technique for processing **contiguous** segments (subarrays or substrings) in  time.

### **Patterns & Triggers**

| Pattern | Mental Trigger | Strategy |
| --- | --- | --- |
| **Fixed Window** | "Find an anagram/permutation" or "Given a specific length **K**." | Maintain a window of size **K**. As the right pointer moves, the left pointer **must** follow immediately. |
| **Variable Window** | "Find the **longest/shortest** subarray" or "Find the **minimum** window." | Expand the right pointer to find a valid window. Once valid (or invalid), shrink the left pointer to optimize or repair. |

---

### **Pattern Breakdown**

#### **1. Fixed Window (The "Slinky" Move)**

Use this when the window size is predetermined.

* **The Recognition:**
    * The problem involves a continuous range.
    * The constraint is based on a **fixed length**.
    * *Example:* In "Permutation in String," a permutation of `s1` must be exactly `len(s1)`. Therefore, your window is always `len(s1)`.


* **The Implementation:**
    1. Build the initial window (first `K` elements).
    2. Loop from `K` to `N`.
    3. Add `nums[i]`, remove `nums[i - K]`.

#### **2. Variable/Dynamic Window (The "Accordion" Move)**

Use this when the window size depends on the content of the elements.

* **The Recognition:**
    * The problem asks for a **min/max length** to satisfy a condition.
    * *Example:* "Find the longest subarray with unique characters."


* **The Implementation:**
    1. Expand the `right` pointer to include an element.
    2. Use a `while` loop to shrink the `left` pointer until the condition is met again.

### General Sliding Window Pattern

Most sliding window problems follow a consistent logical flow. Use this pattern to maintain a valid window while traversing the data:

1.  **Expand**: Add a new element to the window from the right.
2.  **Validate**: Check if the window is currently valid based on the problem constraints. Examples of constraints include:
    -   Must have at least 2 different characters.
    -   Sum should be a multiple of 10.
    -   Must contain at least 5 characters.
    -   Must be an anagram or palindrome of a specific target.
3.  **Shrink**: If the window becomes **invalid**, move the `left` pointer to remove elements until the window satisfies the constraints again.
4.  **Measure**: Once the window is valid, record the size (`right - left + 1`) or any other required property.
5.  **Repeat**: Continue adding elements from the right until you have processed the entire input.

#### Pseudocode Template

```python
left = 0
ans = 0
current_state = 0 # Can be a sum, frequency map, etc.

for right in range(len(nums)):
    # 1. Expand: Add the rightmost element
    current_state += nums[right]
    
    # 2 & 3. Validate and Shrink: While the condition is violated
    while not is_valid(current_state):
        current_state -= nums[left]
        left += 1
        
    # 4. Measure: Record the result for this valid window
    ans = max(ans, right - left + 1)

return ans
```


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

* [557. Reverse Words in a String III](./reverseWords.py) - https://leetcode.com/problems/reverse-words-in-a-string-iii/
* [917. Reverse Only Letters](./reverseOnlyLetters.py) - https://leetcode.com/problems/reverse-only-letters/
* [2540. Minimum Common Value](./minCommonValue.py) - https://leetcode.com/problems/minimum-common-value/
* [283. Move Zeroes](./moveZeroes.py) - https://leetcode.com/problems/move-zeroes/
* [2000. Reverse Prefix of Word](./reversePrefix.py) - https://leetcode.com/problems/reverse-prefix-of-word/

### Sliding Window

* [209. Minimum Size Subarray Sum](./minSizeSubarraySum.py) - https://leetcode.com/problems/minimum-size-subarray-sum/
    - good problem to review
* [1456. Maximum Number of Vowels in a Substring of Given Length](./maxVowels.py) - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
    - good problem to review
* [1208. Get Equal Substrings Within Budget](./equalSubstrings.py) - https://leetcode.com/problems/get-equal-substrings-within-budget/
    - good problem to review

### Prefix Sum

* [1732. Find the Highest Altitude](./highestAltitude.py) - https://leetcode.com/problems/find-the-highest-altitude/
* [724. Find Pivot Index](./pivotIndex.py) - https://leetcode.com/problems/find-pivot-index/
    - good problem to review
* [303. Range Sum Query - Immutable](./rangeSumImmutable.py) - https://leetcode.com/problems/range-sum-query-immutable/
    - some notes about prefix sum, good to at least check the docstrings but not redo the problem

