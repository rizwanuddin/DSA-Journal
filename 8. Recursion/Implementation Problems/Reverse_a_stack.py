"""
Reverse a Stack

You are given a stack of integers. Your task is to reverse the 
stack using recursion. You may only use standard stack operations 
(push, pop, top/peek, isEmpty). You are not allowed to use any loop 
constructs or additional data structures like arrays or queues. 
Your solution must modify the input stack in-place to reverse the 
order of its elements.

Example 1:
Input: stack = [4, 1, 3, 2]
Output: [2, 3, 1, 4]

Example 2:
Input: stack = [10, 20, -5, 7, 15]
Output: [15, 7, -5, 20, 10]



# REVERSE A STACK — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given a stack, and I
need to reverse the order of its elements in place, using only
recursion and standard stack operations — no loops, and no extra
array or queue."

## 2. BRUTE FORCE

"Normally I'd just pop everything into an array, reverse the array,
and push it all back. But that uses an extra data structure, which
isn't allowed here, so I need a way to do this using only the call
stack itself as my temporary storage."

## 3. OPTIMIZE

"Since I can only access the top of the stack, the real challenge is
getting an element to the bottom. I'll write a helper function whose
only job is sinking one item to the bottom of a stack, using
recursion to dig past everything above it and put it back after."

## 4. KEY OBSERVATION

"There are two separate recursive jobs here. One function pops the
top element and reverses everything below it. The other function
takes one element and sinks it to the bottom of whatever stack
currently exists, restoring everything it moved out of the way
afterward."

## 5. APPROACH

"First, I'll write insertAtBottom, which takes a stack and an item.
If the stack is empty, I push the item — it's now the only element,
so it's automatically at the bottom. Otherwise, I pop the top, call
insertAtBottom again on what's left, then push that popped element
back once the item is placed below it.

Then, my main function pops the top of the stack, recursively
reverses everything below it, and once that's done, calls
insertAtBottom to sink the original top element to the very bottom."

## 6. WHILE CODING

"First, I write my helper for sinking one item to the bottom of a
stack."

def insertAtBottom(stack, item):

"If the stack is empty, there's nothing in the way, so I push the
item right here."

    if len(stack) == 0:
        stack.append(item)
        return

"Otherwise, I pop the top to get it out of the way temporarily."

    top = stack.pop()

"I recurse to keep digging toward the bottom."

    insertAtBottom(stack, item)

"Once the item is placed, I restore the element I popped, right back
on top."

    stack.append(top)

"Now my main reversal function."

def helper(stack):

"A stack of 0 or 1 elements is already reversed, so that's my base
case."

    if len(stack) <= 1:
        return

"Otherwise, I pop the top and hold onto it."

    top = stack.pop()

"I recursively reverse everything below it first."

    helper(stack)

"Once that's reversed, I sink the original top element to the
bottom."

    insertAtBottom(stack, top)

"I call helper on the input stack to kick it off, modifying it in
place."

helper(stack)

## 7. EDGE CASES

"If the stack is empty or has only one element, the base case
handles it immediately, since a stack that small is already its own
reverse."

"Since I'm modifying the stack in place using append and pop, no
extra data structure is ever created, which satisfies the
constraint."

## 8. COMPLEXITY

"Time complexity is O(n squared). The main function makes n calls,
and each one calls insertAtBottom, which itself takes up to O(n) time
depending on how deep it has to dig, so the total work adds up
quadratically.

Space complexity is O(n), due to the recursion stack depth from both
functions combined."
"""
class Solution:
    def reverseStack(self, stack):

        def insertAtBottom(stack, item):
            # Base case: stack is empty, item becomes the only element
            if len(stack) == 0:
                stack.append(item)
                return

            # Pop top, recurse to place item deeper, then restore top
            top = stack.pop()
            insertAtBottom(stack, item)
            stack.append(top)

        def helper(stack):
            # Base case: 0 or 1 elements is already "reversed"
            if len(stack) <= 1:
                return

            # Pop top, reverse everything below it, then sink top to the bottom
            top = stack.pop()
            helper(stack)
            insertAtBottom(stack, top)

        helper(stack)