"""
Top K Frequent Elements

Given an integer array nums and an integer k, return any order list of the k most frequent 
elements in nums.
Your solution must run in better than O(n log n) time, where n = nums.length.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears once.
The two most-frequent elements are 1 and 2.

Example 2:
Input: nums = [4,4,6,6,7], k = 2
Output: [4,6]
Explanation: 4 and 6 both occur twice (highest), 7 occurs once.



# Top K Frequent Elements: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given an array of numbers and a number k.
I need to return the k numbers that appear the most times."

"Quick things I'd confirm:
can I return them in any order? I'll assume yes.
Is the answer always unique, so there's no tie at the cutoff? I'll assume yes.
Is k always between 1 and the number of distinct numbers? I'll assume yes."

"So the first thing I need, no matter what,
is how many times each number appears.
For that, I'll use a hashmap, number to count.
That part is the same in every approach."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll count every number with a hashmap.
Then I take all the distinct numbers,
and sort them by their count, from biggest to smallest.
Then I return the first k. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"First portion, counting.
I go through all n numbers once, and each hashmap update is big O of 1.
So that's big O of n."

"Next portion, sorting the distinct numbers.
To ease out computations, I'll say d is the number of distinct numbers.
Can I say d is at most n? I can.
Sorting d numbers takes d logarithmic of d.
In the worst case, every number is different, so it's n log n."

"Taking the first k is big O of k."

"So the overall time complexity is n plus d log d,
which is near about big O of n log n in the worst case."

### Space complexity

"Am I using any extra space?
The hashmap holds d keys, and the sorted list holds d numbers.
So that's big O of n in the worst case."

"Obviously the interviewer will not be happy with n log n,
and he'll ask me to optimize."

## Heap approach

"Instead of fully sorting everything,
I only need the top k, right?
So I'll use a heap.
In case you don't know about it, nothing to worry about.
Just remember, it gives me the minimum value every time.
I want the biggest count, so I store the count as negative,
and the most frequent number sits right at the top."

"What is the next step?
I put every distinct number in a list, as (negative count, number).
Then I heapify it.
Then I pop k times, and each pop gives me the next most frequent number."

### Time complexity

"First portion, counting, that's big O of n."

"Next portion, building the list of d pairs, that's big O of d.
Heapify is also big O of d,
because most of the elements are near the bottom and barely move."

"Next portion, popping k times.
Each pop is logarithmic of d.
So that's k logarithmic of d."

"So the overall time complexity is n plus d plus d plus k log d.
Since d is at most n, that's near about big O of n plus k log n."

### Space complexity

"The hashmap is big O of d, the heap is big O of d,
and the results are big O of k.
So overall, it's big O of n in the worst case."

"This is better than sorting,
but there's still a log in there.
Can I get rid of it completely? I can."

## Optimal

"Here's the key thing I notice.
What's the biggest count a number can have?
At most n, right? If every number in the array is the same.
And the smallest count is 1."

"So every count is a number between 1 and n.
That means instead of sorting by count,
I can just put each number into a slot for its count."

"This is called bucket sort.
In case you don't know about it, nothing to worry about.
Just remember, it's a list of lists,
where index i holds every number that appears exactly i times."

"What is the next step?
I make a list of n + 1 empty lists.
I make n + 1 so that index n exists, and I never use index 0."

"Then for every number in the hashmap,
I put it into buckets at its count."

"Now I go through the buckets from the biggest count, n, down to 1.
For each number in that bucket, I add it to the results.
As soon as I have k numbers, I return. Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"First portion, counting.
I go through all n numbers once, so that's big O of n."

"Next portion, making the buckets.
That's n + 1 empty lists, so big O of n."

"Next portion, filling the buckets.
I go through every distinct number once,
and putting it into a bucket is just an index lookup and an append.
So that's big O of d, which is at most n."

"Next portion, the last loop.
This one has a for loop inside a for loop, so it looks scary, right?
But let's think about it.
The outer loop goes over n + 1 buckets, so that's big O of n.
And the inner loop, across all the buckets combined,
only ever touches each distinct number once,
because each number lives in exactly one bucket.
So it's n plus d in total, not n into d."

"So the overall time complexity is
n plus n plus d plus n plus d,
which is nothing but big O of n."

"If I compare,
the brute force was n log n,
the heap was n plus k log n,
and now it's just n. No log at all."

### Space complexity

"What about the space complexity?
The hashmap is big O of d.
The buckets have n + 1 slots,
and together they hold d numbers, so that's big O of n.
The results are big O of k.
So the overall space is big O of n."

## Code

### Heap

"First, I build count, an empty dictionary.
For every num in nums, if it's already in count, I add 1.
Otherwise, I set it to 1."

"Then I make an empty list called heap.
For every num in count, I append (negative count[num], num).
The negative makes the most frequent number come out first."

"Then I call heapq.heapify on heap."

"Then I make an empty list called results,
and loop k times.
Each time, I pop the top, unpack it into freq and num,
and append num to results."

"Finally, I return results."

### Bucket sort

"First, I build count the same way."

"Then I make buckets, a list of len(nums) + 1 empty lists."

"For every num in count,
I append num into buckets[count[num]].
So the number goes into the slot for how many times it appears."

"Then I make an empty list called results."

"I loop freq from len(nums) down to 1, going backward,
because I want the biggest counts first."

"For every num in buckets[freq], I append it to results.
Then I check, is the length of results equal to k?
If yes, I return results right away."

"I return inside the loop,
so I stop as soon as I have k numbers,
and I don't waste time on the smaller buckets."

## Quick check

```
nums = [1, 1, 1, 2, 2, 3], k = 2

- "count is 1:3, 2:2, 3:1."
- "Heap: the list is (-3, 1), (-2, 2), (-1, 3).
  The first pop gives 1, and the second gives 2. The result is [1, 2]. Correct."
- "Bucket sort: there are 7 buckets, for indexes 0 to 6.
  1 goes into bucket 3, 2 goes into bucket 2, and 3 goes into bucket 1."
- "I go from 6 down. 6, 5, and 4 are empty.
  Bucket 3 has 1, so results is [1].
  Bucket 2 has 2, so results is [1, 2].
  That's k = 2, so I return [1, 2]. Perfect."

```
nums = [1], k = 1
```

- "count is 1:1. 1 goes into bucket 1.
  I loop down to 1, add it, and return [1]. Correct."
"""
#BETTER APPROACH WITH HEAP 
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = {}                                  # SPACE O(n): one key per distinct number
        for num in nums:                            # TIME O(n)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1                      # fixed: 1, not 0

        heap = []                                   # SPACE O(n)
        for num in count:                           # TIME O(n): up to n distinct numbers
            heap.append((-count[num], num))         # O(1) each
        heapq.heapify(heap)                         # TIME O(n)

        results = []                                # SPACE O(k)
        for _ in range(k):                          # k pops
            freq, num = heapq.heappop(heap)         # O(log n) each -> O(k log n)
            results.append(num)
        return results

        # TOTAL TIME:  O(n) + O(n) + O(n) + O(k log n) = O(n + k log n)
        # TOTAL SPACE: O(n) [count] + O(n) [heap] + O(k) [results] = O(n)


#BUCKET SORT - THE MOST OPTIMAL ONE 
class Solution:
    def topKFrequent(self, nums, k):
        # n = len(nums)

        count = {}                                       # SPACE O(n): at most n distinct keys
        for num in nums:                                 # TIME O(n): one pass
            if num in count:
                count[num] += 1                          # O(1)
            else:
                count[num] = 1                           # O(1)

        buckets = [[] for _ in range(len(nums) + 1)]     # TIME O(n), SPACE O(n): n+1 slots
        for num in count:                                # TIME O(n): at most n distinct numbers
            buckets[count[num]].append(num)              # O(1): index lookup + append

        results = []                                     # SPACE O(k)
        for freq in range(len(nums), 0, -1):             # TIME O(n): at most n slots
            for num in buckets[freq]:                    # across ALL slots, each number visited once
                results.append(num)                      # O(1)
                if len(results) == k:                    # O(1)
                    return results
        return results

        # TOTAL TIME:  O(n) + O(n) + O(n) + O(n) = O(n)
        # TOTAL SPACE: O(n) [count] + O(n) [buckets] + O(k) [results] = O(n)          

