"""
Evaluate Reverse Polish Notation - Explanation

You are given an array of strings tokens that represents a valid 
arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
    The operands may be integers or the results of other operations
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward 
    zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5




## Evaluate Reverse Polish Notation

**Clarify:**
- Tokens represent a valid RPN expression — numbers and operators (+, -, *, /)
- Evaluate it and return a single integer result
- Division truncates toward zero (not regular floor division)

**Brute force:**
- Not really a "brute force vs optimize" problem — the stack approach IS the natural/only reasonable approach here, since RPN is defined by how a stack processes it

**Optimize:**
- N/A — one clean O(n) pass with a stack is already optimal

**Key observation:**
- In RPN, when you hit an operator, it always applies to the two MOST RECENTLY seen numbers — that's exactly stack behavior (LIFO)
- Order matters for pop: the SECOND popped value is num1 (the earlier operand), the FIRST popped value is num2 (the later operand) — this matters a lot for non-commutative operations like subtraction and division

**Approach:**
- stack = []
- for each token:
  - if it's a number: push it onto the stack (as an int)
  - if it's an operator: pop twice (num2 first, then num1), apply the operator as num1 OP num2, push the result back
- after the loop, the single remaining value on the stack is the answer

**While coding:**
- num2 must be popped BEFORE num1 — since stack.pop() gives the most recently pushed value first, and that's actually the second operand in the expression, not the first
- Division must truncate toward zero, not just floor — int(num1 / num2) handles this correctly in Python, since int() truncates toward zero, unlike // which floors toward negative infinity (matters for negative results)
- Return stack[-1] (or stack.pop()) — a single integer, not the whole stack

**Edge cases:**
- Single number with no operators → stack has one element from the start, returned directly
- Negative intermediate results → truncation behavior (int() vs //) becomes important here specifically

**Complexity:**
- Time: O(n) — one pass through tokens
- Space: O(n) — worst case, stack holds up to n/2 numbers before any operator appears
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []
        num1 = 0
        num2 = 0
        value = 0
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == "+":
                    value = num1 + num2
                elif char == "-":
                    value = num1 - num2
                elif char == "*":
                    value = num1 * num2
                else:
                    value = int(num1 / num2)
                stack.append(value)
        return stack[-1]


"""
## What is RPN (Reverse Polish Notation)?

- Normal math writes operators BETWEEN operands: `(1 + 2) * 3`
- RPN writes operators AFTER their operands: `1 2 + 3 *`
- No parentheses needed — the order of tokens alone tells you exactly what to do and when

## How to solve it

- Use a stack
- Walk through the tokens left to right:
  - number → push it onto the stack
  - operator → pop the top TWO numbers off the stack, apply the operator, push the result back
- Popping order matters: the value popped FIRST is the second operand, the value popped SECOND is the first operand (important for - and /)
- After processing every token, the one value left on the stack is the final answer
"""

