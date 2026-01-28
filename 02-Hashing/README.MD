# 02-Hashing

### Core Concepts

* **Hash Function**: Takes an input and converts it to an integer. This integer is mapped to a fixed-size index (often called **buckets**) set by the programmer.
* **Dictionary**: A collection of **key-value pairs**.
* **Keys**: Can be almost anything, but they **must be immutable** (e.g., strings, integers, tuples).


* **Hash Map**: An unordered data structure that stores key-value pairs.
* **Efficiency**: Adds, removes, and checks for keys in $O(1)$ average time.
* **Functionality**: Can update values and iterate through both keys and values simultaneously.
* **Trade-off**: Faster than arrays for lookups but consumes more space ($O(N)$).


* **Hash Set**: Use specifically when you only need to check if an element **exists**.
* **Efficiency**: Add, remove, and check in $O(1)$ average time.
* **Uniqueness**: A set only stores unique elements; it automatically handles duplicates.


> **Note:** In the context of LeetCode, we rarely deal with the hash function itself. It happens "under the hood" whenever we create a pair or perform a lookup.

---

## Key Optimizations
> **The "If-In" Rule:** Anytime you find your algorithm running `if ... in ...` on a list, consider using a **Hash Set** or **Hash Map** to store elements. This converts an $O(N)$ search into an $O(1)$ lookup, which can reduce total complexity from $O(N^2)$ to $O(N)$.

---

## Checking For Existence

### Example Problems Below

* [Isolated Numbers](./CheckingForExistence/EX_findIsolatedNumbers.py)
* [First Repeated Character](./CheckingForExistence/EX_repeatedCharacter.py)
* [Two Sum](./CheckingForExistence/EX_twoSum.py)

### Practice Problems for Testing

* [1832. Check if the Sentence Is Pangram](./CheckingForExistence/checkIfPangram.py) 
* [1426. Counting Elements](./CheckingForExistence/countElements.py) 
* [268. Missing Number](./CheckingForExistence/missingNumber.py) 

---

## Counting

If you need to track the frequency of elements (how many times each number or character appears), a **Hash Map** is the most efficient tool.

* **Logic**: The **Key** is the element itself, and the **Value** is its current count.
* **The `defaultdict` (from `collections`)**: Automates key initialization. When you access a missing key, it creates it with a default value (like `0` for `int`), preventing `KeyErrors`.
* **Important Note**: When using `len(counts)` to track distinct elements, you must use `del counts[key]` when a count reaches `0`. Even if a value is `0`, the key still exists in the map and will be counted.

### Subarrays with Exact Constraints (Prefix Sum + Hashing)

When a problem asks for a subarray with an **exact** sum or count (and the array contains negative numbers or zeros), sliding window fails. Instead, use a hash map to store the frequency of prefix sums.

* **The Formula**: `ans += counts[curr - k]`. This checks how many times a prefix sum has occurred in the past that would create a "gap" equal to k when subtracted from our current total.
* **Base Case**: Always initialize `counts[0] = 1` to account for subarrays that start at index 0.

### Example Problems

* [Longest Substring with K Distinct Characters](./Counting/EX_findLongestSubstring.py) — *Uses `defaultdict` and sliding window.*
* [2248. Intersection of Multiple Arrays](./Counting/intersectionArrays.py) — *Uses counts to find elements present in all N arrays.*
* [1941. Equal Number of Occurrences](./Counting/occurencesEqual.py) — *Uses `counts.values()` and `set()` to verify frequencies.*
* [560. Subarray Sum Equals K](./Counting/subarraySumK.py) — *The standard Prefix Sum + Hashing implementation.*
* [1248. Count Number of Nice Subarrays](./Counting/niceSubarrays.py) — *Transforms odds/evens into 1s/0s to use the same logic.*

### Practice Problems for Testing

* [2225. Find Players with Zero or One Losses](./Counting/findWinners.py) - https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
    - a good problem to review
* [1133. Largest Unique Number](./Counting/largestUniqueNumber.py) - https://leetcode.com/problems/largest-unique-number/description/
* [1189. Max number of balloons](./Counting/maxNumberBalloons.py) - https://leetcode.com/problems/maximum-number-of-balloons/description/
    - a good problem to review
* [525.Contiguous Array](./Counting/contiguousArray.py) - https://leetcode.com/problems/contiguous-array/description/
    - a good problem to review 

## Other Hashing Patterns & Variations (all good problems to review)

### 1. The "Grouping by Fingerprint" Pattern

*Used when items that look different belong together because they share a hidden trait.*

* **[49. Group Anagrams](./Other/EX_groupAnagrams.py)**
    * **The Key**: Since anagrams have the same characters, we "normalize" them by sorting: `tuple(sorted(word))`.
    * **The Logic**: Use `defaultdict(list)` to store the original words under their sorted "fingerprint."


* **[2342. Max Sum of a Pair With Equal Sum of Digits](./Other/EX_maxSum.py)**
    * **The Key**: The sum of digits (e.g.,  and ).
    * **Math Trick**: Use `num % 10` to get the last digit and `num //= 10` to strip it.
    * **The "One-Pass" Optimization**: Instead of storing all numbers in a list, only store the **single largest** number seen for that digit sum. When a new number arrives, pair it with the stored "champion" to update your global maximum.


### 2. Tracking Indices: "First Seen" vs. "Last Seen"

*Used to find the size of subarrays based on occurrences.*

* **[2260. Minimum Consecutive Cards to Pick Up](./Other/EX_minimumCardPickup.py) (Shortest Distance)**
    * **Strategy**: Use **Last Seen**.
    * **Shortest Distance**: We want the "start line" to be the **most recent** time we saw the element so the gap is as small as possible. (Update the index every time).
    * **Longest Distance**: We want the "start line" to be the **very first** time the element appeared so the gap is as wide as possible. (Never update the index). Look at the contiguousArray example from the counting section where we set 0 as -1 (we never update that)

    * **Logic**: Always update the dictionary with the current index: `dic[card] = i`.
    * **Formula**: `Current_Index - Last_Index + 1` (The `+1` counts the total elements).

### 3. 2D Cross-Referencing

*Used when comparing rows to columns or other grid patterns.*

* **[2352. Equal Row and Column Pairs](./Other/EX_equalPairs.py)**
    * **The "Vertical" Trick**: Extract columns using a nested loop (fixed `col`, varying `row`) or a list comprehension: `tuple(grid[r][c] for r in range(n))`.
    * **The Multiplication Rule**: If a pattern appears X times as a row and Y times as a column, there are X * Y total pairs.
    * **Optimized Logic**: Hash all rows first, then iterate through columns and check against the row map. `ans += row_counts[current_col]`.

### Other Testing Problems

* [Ransom Note](./Other/ransomNote.py) 
* [Jewels and Stones](./Other/numJewelsInStones.py) - reviewing sets 
* [Longest Substring without Repeating Characters](./Other/lengthOfLongestSubstring.py) - good for sliding window + hashing (similar to findlongestsubstring example from the Counting Section)


## List of More Testing Hashing Problems




