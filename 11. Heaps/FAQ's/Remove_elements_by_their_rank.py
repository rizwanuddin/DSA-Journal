"""
Replace Elements by Their Rank

Given an array of N integers, replace each element by its rank in the array. The rank is defined as the position 
of the 
element in the sorted unique array (1-based).

Smaller numbers have smaller ranks.
Duplicate elements have the same rank.
The output array should contain the ranks corresponding to each element in the original order.

Example 1:
Input: arr = [20, 15, 26, 2, 98, 6]
Output: [4, 3, 5, 1, 6, 2]
Explanation:
Sorted unique array is [2, 6, 15, 20, 26, 98]
Ranks: 2 → 1, 6 → 2, 15 → 3, 20 → 4, 26 → 5, 98 → 6

Example 2:
Input: arr = [1, 5, 8, 15, 8, 25, 9]
Output: [1, 2, 3, 5, 3, 6, 4]
Explanation:
Sorted unique array: [1, 5, 8, 9, 15, 25]
Ranks: 1 → 1, 5 → 2, 8 → 3, 9 → 4, 15 → 5, 25 → 6



# Replace Elements by Their Rank: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given an array of integers.
I need to replace every element with its rank.
The smallest element gets rank 1, the next smallest gets rank 2, and so on."

"If two elements are equal, can I say they get the same rank? I can.
And the next bigger element just gets the next rank, no gaps."

"Quick things I'd confirm:
equal values share a rank? I'll assume yes.
Ranks start from 1? I'll assume yes.
Can it be empty? Then I return an empty array."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"For every element, I'll go through the whole array,
and figure out how many distinct elements are smaller than it.
Why distinct? Because duplicates don't push the rank up, right?"

"So for element arr[i], I'll take a set,
and every time I see something smaller than arr[i], I add it to the set.
At the end, the size of the set plus 1 is the rank of arr[i].
I put that into the answer array. Super simple."

### Time complexity

"Now what will be the time complexity?"

"I have an outer loop that goes through every element, that's big O of n.
For every element, I have an inner loop that goes through the whole array again,
that's another big O of n.
Adding into a set is big O of 1 on average.
So the overall time complexity is nothing but n into n, which is big O of n square."

### Space complexity

"Am I using any extra space?
I'm using a set that can hold up to n elements, that's big O of n.
And the answer array is big O of n.
So the space is somewhere in terms of big O of n."

"Obviously the interviewer will not be happy with n square,
and he'll ask me to optimize."

## Optimal

"In order to optimize, I'll be using a minimum heap.
In case you don't know about it, nothing to worry about.
Just remember, it always gives me the minimum value."

"Here's the idea.
If I could go through the elements from smallest to biggest,
the ranking becomes super simple, right?
The first one gets rank 1.
Every time I see a new bigger value, rank goes up by 1.
If the value is the same as the previous one, rank stays the same."

"But I can't lose track of where each element was.
So I'll store a pair, the value and its original index.
The heap compares by the value first,
and if two values are equal, it compares the index, which is just a number."

"What is the next step?
I push every pair into the heap."

"Then I keep a rank, starting at 0,
and a prev, which is the last value I saw, starting at None."

"Now I pop from the heap.
I get the smallest value and its index.
If this value is different from prev, it's a new value, so I increase the rank.
If it's the same as prev, it's a duplicate, so the rank stays."

"Then I put the rank into the answer at that original index,
and update prev to this value."

"I keep doing this till the heap is empty.
Done and dusted, the answer array has every rank in the right spot."

### Time complexity

"Now let's discuss the time complexity."

"First portion, I have a for loop that pushes every element.
That runs n times.
Each push takes logarithmic of the size of the heap, which goes up to n.
So this portion is n into logarithmic of n."

"Next portion, the while loop.
For how many times is it running?
It runs till the heap is empty, and I pop one element each time.
So it runs n times, agreed?
Inside, I do one pop, which is logarithmic of n.
Everything else, the comparison, the assignment, updating prev,
is big O of 1."

"So the while loop is also n into logarithmic of n."

"So the overall time complexity is n log n plus n log n,
which is two into n log n, so near about big O of n log n."

"If I compare with the brute force,
that was n square, and now it's n log n. That's much better."

### Space complexity

"What about the space complexity?
The answer array is big O of n.
The heap holds all n pairs, that's another big O of n.
So the overall space is big O of n plus big O of n,
which is nothing but big O of n."

## Code

"First, I make the answer array, with a 0 for every element."

"Then I make an empty list called pq, that's my min-heap."

"I loop over every index i,
and push the pair arr[i], i into pq."

"Then I set rank to 0, and prev to None.
None works here, because no real value will ever equal None,
so the first value always counts as new."

"Now I loop while pq is not empty."

"Inside, I pop the minimum, and unpack it into val and ind."

"If val is not equal to prev, it's a new value, so I add 1 to rank."

"Then I set ans at index ind to rank.
I use ind, so the rank goes back into the original position."

"Then I set prev to val."

"Once the heap is empty, I return ans."

## Quick check

```
arr = [20, 15, 26, 2, 98, 6]
```

- "The pops come out in this order: 2, 6, 15, 20, 26, 98."
- "Each one is new, so the ranks go 1, 2, 3, 4, 5, 6."
- "I put each rank back at its original index.
  So the answer is [4, 3, 5, 1, 6, 2]. Perfect."

```
arr = [2, 2, 1]
```

- "I pop 1, so rank becomes 1, and index 2 gets 1."
- "I pop 2 from index 0. It's new, so rank becomes 2."
- "I pop the other 2. It's the same as prev, so rank stays 2."
- "The answer is [2, 2, 1]. Correct."

"Empty array: nothing gets pushed, so I return []."

"One thing I'd mention.
Sorting a copy and using a hashmap from value to rank
is also n log n time and n space.
So the heap and the sort are the same complexity.
Either one is fine."
"""
import heapq

class Solution:
    def ReplaceRank(self, arr):
        ans = [0] * len(arr)            # SPACE: n slots -> O(n)
        pq = []                         # SPACE: holds all n pairs -> O(n)

        # TIME: n pushes x O(log n) each -> O(n log n)
        for i in range(len(arr)):
            heapq.heappush(pq, (arr[i], i))     # O(log n), sift up

        rank = 0
        prev = None

        # TIME: n pops x O(log n) each -> O(n log n)
        while pq:
            val, ind = heapq.heappop(pq)        # O(log n), sift down
            if val != prev:                     # O(1)
                rank += 1                       # O(1)
            ans[ind] = rank                     # O(1), direct index
            prev = val                          # O(1)

        return ans
        # TOTAL TIME:  O(n log n) + O(n log n) -> O(n log n)
        # TOTAL SPACE: O(n) + O(n)             -> O(n)


