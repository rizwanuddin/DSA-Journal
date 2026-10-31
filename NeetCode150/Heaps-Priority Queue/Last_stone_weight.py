"""
Last Stone Weight - Easy

You are given an array of integers stones where stones[i] represents the weight of the ith stone.
We want to run a simulation on the stones as follows:
At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.
Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1




# Last Stone Weight: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a list of stone weights.
Each turn, I take the two heaviest stones and smash them together.
If they weigh the same, both are destroyed.
If they're different, the lighter one is destroyed,
and the heavier one becomes the difference between them.
I keep going until there's at most one stone left.
I need to return the weight of that last stone,
or 0 if there are no stones left."

"I have a few quick questions before I start."

"Are all the weights positive integers?"
→ I'll assume yes.

"Can the list have just one stone?"
→ I'll assume yes, and then I just return it.

"Can the list be empty?"
→ I'll assume it has at least one stone, but I'll still return 0 if it's empty.

"Can I change the input list?"
→ I'll assume I shouldn't, so I'll build my own heap from it.

"Okay, so every turn I need the two biggest stones,
and the list keeps changing as stones get smashed."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
stones = [2, 7, 4, 1, 8, 1]
```

"Smash 8 and 7, which leaves 1. Now I have [2, 4, 1, 1, 1].
Smash 4 and 2, which leaves 2. Now I have [2, 1, 1, 1].
Smash 2 and 1, which leaves 1. Now I have [1, 1, 1].
Smash 1 and 1, which destroys both. Now I have [1].
Answer: 1."

"A few edge cases:"
- "One stone, like [5]: nothing to smash. Answer: 5."
- "Two equal stones, like [3, 3]: both are destroyed. Answer: 0."
- "Two different stones, like [10, 4]: Answer: 6."
- "All the same, like [2, 2, 2, 2]: they cancel in pairs. Answer: 0."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
Every turn, I sort the stones,
take the two biggest from the end,
smash them, and put the leftover back in the list if there is one."

"This works because sorting always puts the two heaviest stones at the end."

"The time is O(n^2 log n).
There can be up to n turns,
and each turn sorts the list, which is O(n log n)."

"The space is O(1) extra if I sort in place,
or O(n) if I copy the list first."

"The problem is that I'm re-sorting the whole list every turn,
when only one or two stones actually changed."

## 4. Optimal solution

"The bottleneck is sorting the whole list every turn
just to find the two biggest stones."

"Instead of sorting every turn,
I can keep the stones in a structure that always gives me the biggest one fast."

"The data structure I'll use is a max-heap,
because it gives me the biggest stone in O(log n),
and putting a stone back is also O(log n)."

"Python's heapq only gives me a min-heap.
So I'll store every weight as a negative number.
The smallest negative is the biggest weight,
so the top of the heap is the heaviest stone."

"As I go, while there are at least two stones,
I pop the heaviest, then pop the next heaviest."

"When they're different, I push back the difference,
as a negative number."

"When they're the same, both are destroyed, so I push nothing."

"At the end, if a stone is left, I return its weight.
If the heap is empty, I return 0."

"The time is O(n log n).
Building the heap is O(n).
There are at most n turns,
and each turn does up to three heap operations, each O(log n)."

"The space is O(n), for the heap."

"So I go from O(n^2 log n) down to O(n log n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import heapq."

"Then I'll make a class called Solution,
and a function called stoneWeight that takes self and stones."

"First, I build a list called heap,
where every stone weight is made negative.
I'm making them negative because heapq is a min-heap,
and I need the biggest stone at the top.
This also makes a new list, so I don't change the input."

"Then I call heapq.heapify on it.
That turns the list into a valid heap in O(n)."

"Now I start a while loop that runs while the heap has more than one stone.
I need at least two stones to smash."

"Inside it, I pop the top of the heap, and flip the sign back.
That's the heaviest stone, and I call it y."

"Then I pop again and flip the sign.
That's the second heaviest, and I call it x."

"y is always bigger than or equal to x,
because I popped it first."

"Then I check if y is not equal to x.
If they're different, the leftover stone weighs y - x.
I push it back as a negative number, so the heap stays a max-heap."

"If they're equal, I don't push anything,
because both stones are destroyed."

"When the loop ends, there's at most one stone left."

"Finally, if the heap isn't empty, I return the top, flipped back to positive.
Otherwise, I return 0."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[2, 7, 4, 1, 8, 1]: the heap has -8, -7, -4, -2, -1, -1.
  I pop 8 and 7. They're different, so I push back -1.
  I pop 4 and 2. I push back -2.
  I pop 2 and 1. I push back -1.
  I pop 1 and 1. They're equal, so nothing goes back.
  One stone is left, -1, so I return 1. That matches."
- "[5]: the loop never runs, so I return 5."
- "[3, 3]: I pop 3 and 3. They're equal, so the heap is empty.
  I return 0."
- "[10, 4]: I pop 10 and 4, and push back -6.
  I return 6."
- "[2, 2, 2, 2]: the first pair cancels, then the second pair cancels.
  The heap is empty, so I return 0."

"The output matches what I expected for all of them."

"To recap, time is O(n log n) and space is O(n)."
"""

import heapq
class Solution():
    def stoneWeight(self, stones):
        heap = [-s for s in stones]
        """ can be written this way aw
        heap = []
        for s in stones:
            heap.append(-s)
        """
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y != x :
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0
        """can be written this way aw
        if len(heap) == 1:
            return -heap[0]
        return 0
        """
