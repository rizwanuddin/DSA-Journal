"""
Power Set

Given an array of integers nums of unique elements. Return all 
possible subsets (power set) of the array.
Do not include the duplicates in the answer.

Example 1:
Input : nums = [1, 2, 3]
Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]

Example 2:
Input : nums = [1, 2]
Output : [ [ ] , [1] , [2] , [1,2] ]




SUBSETS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of numbers.

I need to generate every possible subset of that array.

This includes the empty subset, subsets containing some elements, and
the subset containing all elements."


2. BRUTE FORCE

"The brute-force idea is to consider every possible combination of
elements.

For each element, I basically have two choices:

I can either include it in the current subset or skip it.

Since there are 2 choices for each of n elements, there are 2^n
possible subsets."


3. OPTIMIZE

"Backtracking is a natural way to generate these subsets.

Instead of manually creating every combination, I'll recursively make
an include-or-skip decision for each element.

This lets me explore all possible subsets using a decision tree."


4. KEY OBSERVATION

"The key observation is that every element gives me exactly two choices:

1. INCLUDE the current element.
2. SKIP the current element.

After either choice, I move to the next index.

Once I've made a decision for every element, I've created one complete
subset and can add it to my result."


5. APPROACH

"I'll create a backtracking function that keeps track of:

index   → which element I'm currently deciding on
current → the subset I'm currently building

At every index, I'll first choose to include nums[index].

I'll append it to current and recursively move to the next index.

When that recursive path finishes, I'll pop the element to undo my
choice.

Then I'll explore the second choice, which is skipping that element.

Once index reaches len(nums), I've made a decision for every element,
so I'll add a copy of current to result."


6. WHILE CODING

"I'm creating result to store all the subsets."

result = []

"My recursive function keeps track of which index I'm processing and
the subset I'm currently building."

def backtrack(index, current):

"My base case is when index reaches the length of nums, because that
means I've made an include-or-skip decision for every element."

if index == len(nums):
    result.append(current[:])
    return

"First, I'm exploring the INCLUDE choice."

current.append(nums[index])
backtrack(index + 1, current)

"Now I need to undo that choice before exploring the other branch."

current.pop()

"After removing the element, I'm exploring the SKIP choice."

backtrack(index + 1, current)

"Finally, I'll start at index 0 with an empty subset."

backtrack(0, [])


7. EDGE CASES

"If nums is empty, index is already equal to len(nums), so the base
case immediately adds the empty subset."

if index == len(nums):
    result.append(current[:])
    return

"When I add a completed subset to result, I need to append a COPY of
current."

result.append(current[:])

"I need the copy because current is the same list that I keep modifying
with append and pop during backtracking.

If I appended current directly, multiple entries in result could refer
to the same changing list."

"The pop is also important because it removes the element I included
before I explore the SKIP branch."

current.pop()


8. COMPLEXITY

"There are 2^n possible subsets because every element has two choices:
include or skip.

Creating a copy of each subset can take up to O(n) time.

So the total time complexity is O(n * 2^n).

The recursion depth is O(n), so the auxiliary space complexity is O(n),
not counting the output.

The result itself takes O(n * 2^n) space to store all of the subsets."
"""
class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(index, current):

            # Base case: made a decision for every number
            if index == len(nums):
                result.append(current[:])
                return

            # Choice 1: INCLUDE nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)

            # Undo the choice
            current.pop()

            # Choice 2: SKIP nums[index]
            backtrack(index + 1, current)

        backtrack(0, [])

        return result