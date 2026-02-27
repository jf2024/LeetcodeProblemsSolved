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

## Core Concepts

FIFO: first in first out 
    - think of a line at a food restaurant, the first person orders their food and is the first one to leave the line

in stacks, elements are added and removed from one side
with queues, elements are added from one side and removed from the other side 
    - add elements called enqueue
    - delete elements called dequeue 

can technically use dynamic arrays to implement a queue but will be O(N) when removing or adding from the front of the array (remember each element has a fixed address so if we add or remove, will need to shift oru elements which is O(N) or n is the size of the array)

instead we can use doubly linkedlists since we have pointers instead and with this, our addition or deletion becomes O(1) so its now much more efficient 

moving forward, we will implement a deque, basically a double ended queue
    - with a deque, we can add or remove elements from either side 
    - in a regular queue, usually add elements to one side and delete from the other side 
    "from collections import deque" 

less common problems then stacks as queues are usually for BFS (breath first search) but again outside of that, not rlly used standalone like the previous data structures 

https://docs.python.org/3/library/collections.html#collections.deque 
list of some operations to use like append, appendleft, clear, ect... 