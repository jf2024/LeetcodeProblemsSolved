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

* [Isolated Numbers](./CheckingForExistence/EX_findIsolatedNumbers.py)
* [First Repeated Character](./CheckingForExistence/EX_repeatedCharacter.py)
* [Two Sum](./CheckingForExistence/EX_twoSum.py)

### Practice Problems

* [1832. Check if the Sentence Is Pangram](./CheckingForExistence/checkIfPangram.py) 
* [1426. Counting Elements](./CheckingForExistence/countElements.py) 
* [268. Missing Number](./CheckingForExistence/missingNumber.py) 

---

## Counting

*(in progress...)*
