"""
Maximum Sum Combination

Given two integer arrays nums1 and nums2 and an integer k, return the maximum k valid sum 
combinations from all possible sum combinations using the elements of nums1 and nums2.
A valid sum combination is made by adding one element from nums1 and one element from nums2. 
Return the answer in non-increasing order.

Example 1:
Input: nums1 = [7, 3], nums2 = [1, 6], k = 2
Output: [13, 9]
Explanation:
The 2 maximum combinations are made by:
nums1[0] + nums2[1] = 13
nums1[1] + nums2[1] = 9

Example 2:
Input: nums1 = [3, 4, 5], nums2 = [2, 6, 3], k = 2
Output: [11, 10]

Explanation:
The 2 maximum combinations are made by:
nums1[2] + nums2[1] = 11
nums1[1] + nums2[1] = 10




# Maximum Sum Combinations: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given two arrays, num1 and num2, and a number k.
I can make a sum by picking one element from num1 and one from num2.
I need to return the k largest sums, from biggest to smallest."

"Quick things I'd confirm:
can the same pair of indexes be used twice? I'll assume no, each pair once.
Can two different pairs give the same sum? Yes, and both count.
Is k always at most n into m, the number of possible pairs? I'll assume yes.
Can I change the input arrays? I'll assume yes, since I'm sorting them."

"So the main question is, there are n into m possible pairs,
but I only need the top k. How do I avoid looking at all of them?"

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll make every possible pair.
Two loops, one over num1, one over num2,
and I put every sum into an array."

"Then I sort that array from biggest to smallest,
and return the first k. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"First portion, making all the sums.
num1 has n elements, num2 has m elements,
so the two loops run n into m times.
That's big O of n into m."

"Next portion, sorting.
The array has M elements, where M is nothing but n into m.
Sorting takes M logarithmic of M."

"Then taking the first k is big O of k."

"So the overall time complexity is
n into m, plus M log M, plus k, where M is n into m.
The sort dominates, so it's near about big O of n into m, into log of n into m."

### Space complexity

"Am I using any extra space?
Yes, the array of all sums, that's big O of n into m."

"Obviously the interviewer will not be happy with this,
because I'm building every single pair when I only need k of them,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
If I sort both arrays from biggest to smallest,
then the biggest sum has to be num1[0] plus num2[0], right?"

"Now think of it like a grid.
Row i is num1[i], column j is num2[j].
Every cell is num1[i] plus num2[j].
In each row, as j goes right, the sums only get smaller, agreed?
So each row is already a sorted list, from biggest to smallest."

"So this is nothing but merging sorted lists.
Same idea as merge K sorted lists.
Each row is one list, and I only need the top k."

"So I'll use a heap.
In case you don't know about it, nothing to worry about.
Just remember, it gives me the minimum value every time.
I want the biggest sum, so I store the sum as negative,
and the biggest sum sits right at the top."

"What is the next step?
I push the first element of each row into the heap.
That's num1[i] plus num2[0], for each i.
And I store i and j with it, so I know where it came from."

"But do I need every row? No.
I only need k sums,
so at most the first k rows can ever matter.
So I push min of k and n rows."

"Now I pop k times.
Every pop gives me the next biggest sum, so I add it to the result."

"After I pop a sum from row i, column j,
the next candidate in that row is column j + 1, right?
So if j + 1 is still inside num2, I push num1[i] plus num2[j + 1]."

"Each cell can only be reached from the cell to its left,
so I never push the same pair twice.
That's why I don't need a visited set."

"Once I've popped k times, I return the result. Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"First portion, sorting num1.
That's n logarithmic of n."

"Next portion, sorting num2.
That's m logarithmic of m."

"Next portion, the first loop that fills the heap.
For how many times is it running?
min of k and n times, so at most k.
Each push is logarithmic of the heap size, and the heap has at most k items.
So this portion is near about k logarithmic of k."

"Next portion, the second loop.
It runs exactly k times.
Inside, I do one pop and at most one push.
Every pop takes one out and every push puts one in,
so the heap never grows past k items.
That means each one is logarithmic of k.
So this portion is k into 2 into logarithmic of k,
which is nothing but k log k."

"So the overall time complexity is
n log n, plus m log m, plus k log k, plus k log k,
which is big O of n log n plus m log m plus k log k."

"If I compare with the brute force,
that was n into m, into log of n into m.
Now the k part is only k log k,
so I never touch all n into m pairs.
The sorting is the biggest part now, and that's way smaller."

### Space complexity

"What about the space complexity?
Can I say the heap holds at most k items? I can.
So that's big O of k.
And the result holds k sums, that's another big O of k.
The sorting is in place.
So the overall space is big O of k."

## Code

"First, I sort num1 from biggest to smallest, using reverse = True.
Then I sort num2 the same way."

"Then I make an empty list called heap."

"I loop i from 0 to min of k and the length of num1.
For each i, I push a tuple:
negative of num1[i] plus num2[0], then i, then 0.
The negative makes the biggest sum come out first.
i and 0 tell me which row and column it came from."

"Then I make an empty list called result."

"I loop k times."

"Inside, I pop the top, and unpack it into neg_sum, i, and j.
I append negative neg_sum to result,
which flips it back to the real sum."

"Then I check, is j + 1 still less than the length of num2?
If yes, there's a next candidate in this row.
So I push negative of num1[i] plus num2[j + 1], then i, then j + 1."

"After k pops, I return result."

## Quick check

```
num1 = [3, 2], num2 = [1, 4], k = 2
```

- "After sorting, num1 is [3, 2], and num2 is [4, 1]."
- "I push row 0: 3 + 4 = 7, and row 1: 2 + 4 = 6."
- "I pop 7. Then I push 3 + 1 = 4 from row 0."
- "I pop 6. The result is [7, 6]. Perfect."

```
num1 = [1, 4, 2, 3], num2 = [2, 5, 1, 6], k = 4
```

- "After sorting, num1 is [4, 3, 2, 1], and num2 is [6, 5, 2, 1]."
- "I push the first column: 10, 9, 8, 7."
- "I pop 10, from row 0. Then I push 4 + 5 = 9."
- "I pop 9. There are two 9s, and the tie goes to the smaller i,
  so it's row 0's 9. Then I push 4 + 2 = 6."
- "I pop the other 9, from row 1. Then I push 3 + 5 = 8."
- "I pop 8."
- "The result is [10, 9, 9, 8]. Correct."
"""
import heapq
class Solution:
    def maxCombinations(self, num1, num2, k):
        num1.sort(reverse = True)
        num2.sort(reverse = True)          # O(n log n) + O(m log m)

        heap = []                           # space: at most k items -> O(k)
        for i in range(min(k, len(num1))):  # runs at most k times -> O(k)
            heapq.heappush(heap, (-(num1[i]+num2[0]), i, 0))  # O(log k) each
            # this loop total: O(k log k)

        result = []                          # space: O(k)
        for _ in range(k):                   # runs exactly k times
            neg_sum, i, j = heapq.heappop(heap)   # O(log k)
            result.append(-neg_sum)               # O(1)
            if j + 1 < len(num2):
                heapq.heappush(heap, (-(num1[i]+num2[j+1]), i, j + 1))  # O(log k)
            # this loop total: O(k log k)

        return result

        # TOTAL TIME:  O(n log n) + O(m log m) + O(k log k)
        # TOTAL SPACE: O(k) [heap] + O(k) [result] -> O(k)

