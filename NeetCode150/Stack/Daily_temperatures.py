"""
Daily Temperatures - Explanation

You are given an array of integers temperatures where 
temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after 
the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will 
appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [22,21,20]
Output: [0,0,0]




## Daily Temperatures

**Clarify:**
- Given a list of temperatures, for each day return how many days until a WARMER temperature
- If no warmer day exists later, that day's answer is 0

**Brute force:**
- For each day, scan forward until a warmer day is found
- O(n²) time in the worst case (e.g. strictly decreasing temperatures)

**Optimize:**
- Monotonic stack — store indices, keep the stack values decreasing (temps at those indices go down as you go deeper into the stack)
- O(n) time, each index pushed and popped at most once

**Key observation:**
- Whenever a new temperature is warmer than what's on top of the stack, that top index has just found its answer — pop it and record the day-difference
- Indices left on the stack are "waiting" for a future warmer day — you don't know their answer yet, so they just sit there until one comes along

**Approach:**
- stack = [], result = [0] * len(temperatures)
- for i in range(len(temperatures)):
  - while stack is not empty AND current temp > temp at stack's top index:
    - pop that index off the stack
    - result[popped index] = i - popped index
  - push i onto the stack

**While coding:**
- Store INDICES on the stack, not temperature values — you need the index to know how many days apart, and to write into result[] at the right spot
- The while loop (not if) matters — one new warmer day might resolve MULTIPLE waiting indices at once, not just the most recent one
- Indices still on the stack at the end never found a warmer day — result[] was already initialized to 0, so no extra step needed for them

**Edge cases:**
- Strictly decreasing temperatures → nothing ever gets popped except at the very end, all results stay 0
- Strictly increasing temperatures → every index gets resolved almost immediately, mostly 1s
- Single day → result is just [0]

**Complexity:**
- Time: O(n) — each index is pushed once and popped at most once
- Space: O(n) — worst case (decreasing temps), stack holds every index
"""
class Solution:
    def dailyTemp(self, temperatures):

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                old_index = stack.pop()

                result[old_index] = i - old_index

            stack.append(i)

        return result

            