"""
Subsets - Medium

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]




# Subsets: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a list of numbers.
I need to return every possible subset of it, which is also called the power set.
That includes the empty subset, and the full list itself."

"I have a few quick questions before I start."

"Are all the numbers unique?"
→ I'll assume yes, so I don't need to worry about duplicate subsets.

"Does the order of the subsets matter, or the order inside each subset?"
→ I'll assume neither matters.

"Should the empty subset be included?"
→ I'll assume yes.

"Can the list be empty?"
→ I'll assume yes, and then the answer is just [[]].

"Can the numbers be negative?"
→ I'll assume yes. It doesn't change anything, since I never compare values.

"Roughly how big can the list get?"
→ I'll assume it's small, like 10 or fewer,
because the number of subsets doubles with every number I add.

"Okay, so for every number, I have two choices: take it, or skip it.
I need to try every combination of those choices."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [1, 2, 3]
```
"There are 2^3 = 8 subsets:
[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]."

"A few edge cases:"
- "Empty list: Answer: [[]]."
- "One number, like [0]: Answer: [[], [0]]."
- "Negative numbers, like [-1, 2]: Answer: [[], [-1], [2], [-1, 2]]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"I want to be upfront: there isn't a faster way to do this.
There are 2^n subsets, and each one can have up to n numbers.
Just writing out the answer takes O(n * 2^n) time.
So any correct solution is at least O(n * 2^n)."

"My first idea is the simplest one, using bits.
I count from 0 up to 2^n - 1.
Each number in that range, written in binary, has n bits.
If bit j is 1, I take nums[j]. If it's 0, I skip it.
Every binary number gives me one subset."

"This works because there are exactly 2^n binary numbers with n bits,
and each one is a different take-or-skip combination."

"The time is O(n * 2^n).
There are 2^n numbers, and for each one I check n bits."

"The space is O(n) extra, not counting the output."

"This is already the best big-O.
But it's hard to change for follow-ups,
like when there are duplicates, or when I need to stop early.
So I'd rather use backtracking, which handles those easily."

## 4. Optimal solution

"Since the big-O can't get better,
I want the approach that's clearest and easiest to extend."

"Instead of using bits to stand for take or skip,
I can make that choice directly with recursion."

"I go through the numbers one index at a time.
At each index, I make two calls:
one where I take the number, and one where I skip it."

"The data structures I'll use are a list called subset,
which holds the choices I've made so far,
and a list called res, which holds every finished subset.
I'll use the recursion stack to come back and try the other choice.
That's backtracking."

"As I go, at index i, I add nums[i] to subset,
and go to the next index.
That's the take branch."

"When that call comes back, I remove nums[i] from subset,
and go to the next index again.
That's the skip branch."

"When I reach the end of the list,
I've made a choice for every number,
so I add a copy of subset to res."

"At the end, I return res."

"The time is O(n * 2^n).
The recursion makes 2^n complete subsets,
and copying each one takes up to n steps."

"The space is O(n) extra, for the recursion stack and the current subset.
The output itself takes O(n * 2^n)."

"So it's the same big-O as the bit approach,
which is the best possible, but it's cleaner to extend."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called subsets that takes self and nums."

"I'll create an empty list called subset.
It holds the numbers I've picked so far, in the current path."

"And an empty list called res.
It holds every finished subset."

"Now I'll define a helper called helper that takes i.
i is the index of the number I'm deciding on right now."

"First thing inside it, I check if i equals the length of nums.
If it does, I've made a choice for every number,
so the current subset is complete."

"I append a copy of subset to res.
I make a copy because subset keeps changing as I backtrack.
If I added subset itself, every entry in res would point to the same list,
and they'd all end up empty at the end."

"Then I return, because there are no more numbers to decide on."

"Otherwise, I make the take choice first.
I append nums[i] to subset,
and call helper on i + 1, to decide on the next number."

"When that call comes back, I make the skip choice.
I pop nums[i] off subset, so it's back to how it was before.
That's the backtracking step."

"Then I call helper on i + 1 again,
this time without nums[i] in the subset."

"After defining helper, I call it on 0, to start from the first number."

"Finally, I return res."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[1, 2, 3]: here's the take-or-skip tree.

  ```
                   []
           take 1 /    \ skip 1
               [1]      []
              /   \     /  \
          [1,2]  [1]  [2]   []
          /  \   / \  / \   / \
     [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
  ```

  Each leaf is a finished subset, so I get all 8.
  That matches."
- "Empty list: i is 0, which equals the length,
  so I add a copy of the empty subset. The answer is [[]]."
- "[0]: take 0 gives [0], skip 0 gives []. The answer is [[0], []]."
- "[-1, 2]: the tree works the same way, since I never compare values.
  I get 4 subsets."

"The output matches what I expected for all of them."

"To recap, time is O(n * 2^n) and space is O(n) extra,
plus O(n * 2^n) for the output."

"If the list had duplicates, I'd sort it first.
Then in the skip branch, I'd skip every copy of that same number,
so I never build the same subset twice."
"""
class Solution:
    def subsets(self, nums):
        subset = []
        res = []

        def helper(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            helper(i + 1)

            subset.pop()
            helper(i + 1)

        helper(0)
        return res 