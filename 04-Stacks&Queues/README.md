# 04 - Stacks & Queues

# Stacks

## Core Concepts

- def: ordered collection of elements where you can only add or remove elements from the same end
    - think of a stack of plates, where you can add or remove from the top of the pule 

    - also known as LIFO --> Last In, First Out (make this part bold)

- example: stack = [a, b, c]
    - to add is called push
    - to remove is called pop
    - can also peek, looking at the element at the top of the stack without removal 
        - so if we wanted to pop to our stack, we would have [a, b]
        - if we wanted to push "d" to our stack, it would now be [a, b, d]

- can implement using a dynamic array or linkedlist
    - but usually O(1) for push, pop, random acess 
    - O(N) for search

- some key phrases on when to use stack (sometimes hard to spot)
    - matching elements together
    - querying some property "how far is the next largest element" 
    - evaulate mathematical equation as a string


### Example Problems

* [Valid Parentheses](./Stacks/EX_validParentheses.py)
* [Remove All Adjacent Duplicates in String](./Stacks/EX_removeAdjacentDuplicates.py)
* [Backspace String Compare](./Stacks/EX_BackspaceCompare.py)
    - can also use two pointers to solve this problem


### Testing Problems
* [Simplify Path](./Stacks/simpliftPath.py) - https://leetcode.com/problems/simplify-path/description/
    - good problem to review
* [Make the String Great](./Stacks/makeGoodStrings.py) 

# Queues

add here later 