"""
Min Stack - Explanation

Design a stack class that supports the push, pop, top, and 
getMin operations.
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
Each function should run in O(1)O(1) time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1




## Min Stack

**Clarify:**
- Design a stack supporting push, pop, top, and getMin
- Every operation must run in O(1) time — including getMin, which is the tricky part

**Brute force:**
- getMin() could just scan the whole stack every time to find the minimum
- Works, but that's O(n) for getMin — violates the O(1) requirement

**Optimize:**
- Keep a SECOND stack running in parallel, dedicated to tracking minimums
- Every push updates both stacks together, every pop removes from both together
- This keeps getMin() as a simple O(1) lookup instead of a scan

**Key observation:**
- A single "current minimum" variable isn't enough — once you pop the actual minimum off, you'd have no way to know what the previous minimum was
- Instead, min_stack stores a MINIMUM SNAPSHOT at every single push — "what was the smallest value seen up to and including this push"
- Since min_stack grows and shrinks in perfect sync with the main stack, popping automatically restores the correct previous minimum, like automatic backtracking

**Approach:**
- Two lists: stack (actual values), min_stack (running minimum at each point)
- push(val): append to stack; append min(val, min_stack top) to min_stack (or just val if min_stack is empty)
- pop(): pop from BOTH stacks together, keeps them in sync
- top(): return stack[-1]
- getMin(): return min_stack[-1]

**While coding:**
- Both stacks must always stay the same length — every push/pop touches both, never just one
- Handle the empty min_stack case on the first push (nothing to compare against yet)

**Edge cases:**
- Only one element ever pushed → min_stack has just that one value, getMin trivially correct
- Pushing a new minimum repeatedly → min_stack keeps recording new lower values correctly each time
- Popping back past a previous minimum → min_stack naturally reveals the earlier minimum again, no extra logic needed

**Complexity:**
- Time: O(1) for every operation — push, pop, top, getMin all just touch the end of a list
- Space: O(n) — min_stack grows in parallel with the main stack, same size
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):

        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
