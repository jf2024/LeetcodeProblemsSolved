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

Here is the updated **Counting** section for your README, including the two newest problems and a specific sub-section for the **Prefix Sum + Hashing** pattern you just mastered.

---

## Counting

If you need to track the frequency of elements (how many times each number or character appears), a **Hash Map** is the most efficient tool.

* **Logic**: The **Key** is the element itself, and the **Value** is its current count.
* **The `defaultdict` (from `collections`)**: Automates key initialization. When you access a missing key, it creates it with a default value (like `0` for `int`), preventing `KeyErrors`.
* **Important Note**: When using `len(counts)` to track distinct elements, you must use `del counts[key]` when a count reaches `0`. Even if a value is `0`, the key still exists in the map and will be counted.

### Subarrays with Exact Constraints (Prefix Sum + Hashing)

When a problem asks for a subarray with an **exact** sum or count (and the array contains negative numbers or zeros), sliding window fails. Instead, use a hash map to store the frequency of prefix sums.

* **The Formula**: `ans += counts[curr - k]`.
* **Base Case**: Always initialize `counts[0] = 1` to account for subarrays that start at index 0.

### Example Problems

* [Longest Substring with K Distinct Characters](./Counting/EX_findLongestSubstring.py) — *Uses `defaultdict` and sliding window.*
* [2248. Intersection of Multiple Arrays](./Counting/intersectionArrays.py) — *Uses counts to find elements present in all N arrays.*
* [1941. Equal Number of Occurrences](./Counting/occurencesEqual.py) — *Uses `counts.values()` and `set()` to verify frequencies.*
* [560. Subarray Sum Equals K](./Counting/subarraySumK.py) — *The standard Prefix Sum + Hashing implementation.*
* [1248. Count Number of Nice Subarrays](./Counting/niceSubarrays.py) — *Transforms odds/evens into 1s/0s to use the same logic.*

### Practice Problems for Testing

* add later *