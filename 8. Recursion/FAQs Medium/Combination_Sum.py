"""
Combination Sum

Provided with a goal integer target and an array of unique integers
nums, provide a list of all possible combinations of nums in which 
the selected numbers add up to the target. The combinations can be 
returned in any order. A number may be selected from nums an 
infinite number of times. There are two distinct combinations if 
the frequency of at least one of the selected numbers differs.The 
test cases are created so that, for the given input, there are 
fewer than 150 possible combinations that add up to the target.If 
there is no possible combination, then return an empty vector.

Example 1:
Input : nums = [2, 3, 5, 4] , target = 7
Output : [ [2, 2, 3], [2, 5] , [3, 4] ]
Explanation :
- 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used 
multiple times.
- 2 and 5 are candidates, and 2 + 5 = 7.
- 3 and 4 are candidates, and 3 + 4 = 7.
There are total three combinations.

Example 2:
Input : nums = [2], target = 1
Output : []
Explanation : There is no way we can choose the candidates to sum 
up to target.




# COMBINATION SUM — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array of
unique numbers and a target. I need to find every combination of
numbers that adds up exactly to target. The same number can be reused
as many times as needed, and two combinations are different if the
count of at least one number differs."

## 2. BRUTE FORCE

"The brute-force idea is still to explore include or skip at every
step, like other subsequence problems. The twist here is that
numbers can repeat, so I can't just move forward after using a
number — I need to consider using it again."

## 3. OPTIMIZE

"I'll use the same include or skip recursion, but with one key
change: when I include a number, I stay on the same index instead of
moving forward, since that number is still available for reuse. When
I skip a number, I move to the next index, since I'm done considering
it entirely."

## 4. KEY OBSERVATION

"Include and skip behave differently here than in past problems.
Include keeps the index the same, because reuse is allowed. Skip
moves the index forward, because once skipped, that number is never
considered again in this path. I also need a way to stop paths early
once the sum goes over target, so I don't waste time exploring
combinations that can only get worse."

## 5. APPROACH

"I'll write a helper function tracking the current index, the
running sum, and the combination built so far.

If the running sum equals target, I've found a valid combination, so
I save a copy of it and return.

If the running sum goes over target, or I've run out of numbers to
consider, this path failed, so I return without saving anything.

Otherwise, I try including the current number, staying on the same
index since it can be reused, then undo that choice.

Then I try skipping the current number entirely, moving to the next
index.

I start the recursion at index 0, sum 0, with an empty combination."

## 6. WHILE CODING

"First, I set up a list to collect valid combinations."

result = []

"My helper tracks index, the running sum, and the combination built
so far."

def helper(index, current_sum, current):

"If the sum matches target, I've found a valid combination."

    if current_sum == target:
        result.append(current[:])
        return

"If the sum overshoots target, or there are no more numbers left to
try, this path can't work, so I stop here."

    if current_sum > target or index == len(nums):
        return

"I try including the current number. Since it can be reused, I stay
on the same index for the recursive call."

    current.append(nums[index])
    helper(index, current_sum + nums[index], current)
    current.pop()

"Then I try skipping this number completely, moving to the next
index, since I'm done considering it in this path."

    helper(index + 1, current_sum, current)

"I kick off the recursion at index 0, sum 0, with an empty list."

helper(0, 0, [])
return result

## 7. EDGE CASES

"If no combination can reach target, the result list stays empty,
which matches what the problem expects.

If target is smaller than every number in nums, every include branch
immediately overshoots, so the function correctly returns nothing for
those paths.

Since nums contains unique values, I don't need to worry about
duplicate combinations being generated from equal numbers at
different indices."

## 8. COMPLEXITY

"Time complexity is harder to state simply since it depends on
target and the values in nums, but it's bounded by the number of ways
sums can be formed, which can be exponential in the worst case.

Space complexity is O(target / minimum number) for the recursion
depth in the worst case, since that's how many times the smallest
number could be added before exceeding target."
"""
class Solution:
    def Combination_Sum(self, nums, target):
        result = []
        def helper(index, sum, current):
            if sum == target:
                result.append(current[:])
                return
            if sum > target or index == len(nums):
                return
            current.append(nums[index])
            helper(index, sum + nums[index], current)
            current.pop()

            helper(index + 1, sum, current)
        helper(0, 0, [])