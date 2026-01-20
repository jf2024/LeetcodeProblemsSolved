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

## Checking For Existence

* [Isolated Numbers](./EX_findIsolatedNumbers.py)
* [First Repeated Character](./EX_repeatedCharacter.py)
* [Two Sum](./EX_twoSum.py)

### Practice Problems (TODO LATER)

* [1832. Check if the Sentence Is Pangram](./checkIfPangram.py) 
* [1426. Counting Elements](./countElements.py) 
* [268. Missing Number](./missingNumber.py) 

---

## Counting

*(in progress...)*

