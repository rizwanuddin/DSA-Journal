"""
Hand of Straights

You are given an array of integers hand, where hand[i] is the value on the ith card 
that Alice owns.

Alice wants to split her entire hand into groups such that:

every group contains exactly groupSize cards, and
the card values in each group form a sequence of groupSize consecutive integers 
(e.g. [3, 4, 5], [10, 11, 12, 13]).
Return true if such a rearrangement is possible; otherwise return false.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation:
One possible partition is [1,2,3] [2,3,4] [6,7,8].

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation:
There is no way to split the hand into groups of 4 consecutive cards.





# Hand of Straights: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given an array of cards, called hand,
and a number called groupSize.
I need to check if I can split all the cards into groups,
where every group has exactly groupSize cards,
and the cards in each group are consecutive numbers.
If I can, I return True. Otherwise, False."

"Quick things I'd confirm:
does every card have to be used? I'll assume yes.
Can values repeat? Yes, and that's the whole tricky part.
Can I rearrange the cards in any order? I'll assume yes."

"One thing I notice right away.
If the number of cards is not divisible by groupSize,
can I ever make equal groups? I can't.
So I can return False right there. Super simple."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll sort the hand first.
Now the smallest card is at the front, agreed?"

"The smallest card has to start a group, correct?
Because nothing is smaller than it, so it can't be in the middle of a group."

"So I take the smallest card, say it's x.
Then I search the list for x + 1, remove it,
then search for x + 2, remove it,
and so on till I have groupSize cards.
If any of them is missing, I return False."

"Then I take the next smallest card left,
and do the same thing again,
till the list is empty. Then I return True."

### Time complexity

"Now what will be the time complexity?"

"First portion, the sort.
That's n logarithmic of n."

"Next portion, building the groups.
Every card has to be found and removed once, so that's n removals.
Now, removing from the middle of a list shifts everything after it,
so each removal is big O of n.
And searching for the card is also big O of n.
So this portion is n into n, which is n square."

"So the overall time complexity is n log n plus n square,
which is near about big O of n square."

### Space complexity

"Am I using any extra space?
If I sort and remove on a copy of the hand, that's big O of n.
Nothing else, so the space is big O of n."

"Obviously the interviewer will not be happy with n square,
and he'll ask me to optimize."

## Optimal

"The slow part was searching and removing cards one by one in a list.
So instead of storing every card separately,
I'll just count how many of each card I have."

"I'll use a hashmap, card to count.
Now checking if a card exists, and using one up,
is just big O of 1."

"But I still need to know the smallest card left, every time.
So I'll use a minimum heap.
In case you don't know about it, nothing to worry about.
Just remember, it always gives you the minimum value."

"I'll only push the distinct values into the heap, not every card.
So if 2 shows up three times, the heap only has one 2.
The count lives in the hashmap."

"What is the next step?
I look at the top of the heap, without popping it.
That's the smallest card left, so that's where my next group has to start, right?"

"Let's say it's start.
I go through start, start + 1, till start + groupSize - 1.
For each value, I check: is it in the map, and is its count more than 0?
If not, the group can't be completed, so I return False."

"If it's there, I use one up, so I reduce its count by 1."

"Now if its count becomes 0, that value is completely used up,
so it should leave the heap.
But here's the catch.
It has to be the smallest value in the heap.
If it's not the smallest, that means some smaller value still has cards left.
Those cards need a group that goes through this value,
but this value is gone now.
So it can never be completed, and I return False."

"If it is the smallest, I just pop it."

"I keep doing this till the heap is empty.
If I never hit a problem, I return True. Done and dusted."

### Time complexity

"Now let's discuss the time complexity.
I'll say n is the number of cards,
and k is the number of distinct values.
Can I say k is at most n? I can."

"First portion, the divisibility check.
That's just big O of 1."

"Next portion, building the hashmap.
I go through every card once, and each update is big O of 1.
So this portion is big O of n."

"Next portion, building the heap.
I push k distinct values, and each push is logarithmic of k.
So this portion is k into logarithmic of k."

"Next portion, the while loop.
This one looks scary, because there's a for loop inside a while loop, right?
But let's think about it.
Every time the inner loop runs once, it uses up exactly one card.
And there are only n cards in total.
So across all the rounds, the inner loop runs exactly n times in total, not n square.
Each step inside is big O of 1, so that's big O of n."

"And the pops?
Each distinct value gets popped only once, when its count hits 0.
So that's k pops, each logarithmic of k, so k into logarithmic of k."

"So the overall time complexity is
n plus k log k plus n plus k log k,
which is nothing but big O of n plus k log k."

"In the worst case, every card is different, so k is equal to n.
Then it becomes near about big O of n log n."

"If I compare with the brute force, that was n square.
Now it's n log n at worst. That's much better."

### Space complexity

"What about the space complexity?
The hashmap has one key per distinct value, that's big O of k.
The heap also has only distinct values, that's another big O of k.
So the overall space is big O of k.
In the worst case, k is n, so it's big O of n."

## Code

"First, I check if the length of hand is not divisible by groupSize.
If it's not, I return False right away."

"Then I build freq, an empty dictionary.
For every card, if it's already in freq, I add 1.
Otherwise, I set it to 1."

"Then I make an empty list called pq, that's my min-heap.
I loop over every key in freq, and push it into pq.
So only distinct values go in."

"Now I loop while pq is not empty."

"I set start to pq[0].
I'm only peeking, not popping,
because the value might still have more cards left after this group."

"Then I loop val from start to start + groupSize - 1.
I write it as range of start, start + groupSize,
because the end of range isn't included."

"Inside, if val is not in freq, or freq[val] is 0,
the group is broken, so I return False."

"Otherwise, I reduce freq[val] by 1."

"Then, if freq[val] became 0,
I check if val is not equal to pq[0].
If it's not the smallest, a smaller value is stuck with cards left,
so I return False."

"If it is the smallest, I pop it from pq."

"Once the heap is empty, every card made it into a group,
so I return True."

## Quick check

```
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
```

- "9 cards, and 9 is divisible by 3, so I continue."
- "freq is 1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1."
- "The heap's smallest is 1. I use 1, 2, 3.
  1 hits 0, and it's the top, so I pop it."
- "The smallest is now 2. I use 2, 3, 4.
  2 hits 0 and gets popped, then 3, then 4."
- "The smallest is now 6. I use 6, 7, 8. All three get popped."
- "The heap is empty, so I return True. Perfect."

```
hand = [1, 2, 3, 4, 5], groupSize = 4
```

- "5 cards isn't divisible by 4, so I return False right away. Correct."

```
hand = [1, 1, 2, 3], groupSize = 2
```

- "4 cards, which is divisible by 2."
- "The smallest is 1. I use 1, so its count goes to 1.
  Then I use 2, so its count goes to 0.
  But 2 is not the top, because 1 still has a card left.
  So I return False."
- "That's correct. The leftover 1 would need a 2, but the 2 is already used."
"""
import heapq

class Solution:
    def GroupHand(self, hand, groupSize):
        # n = number of cards, k = number of DISTINCT values (k <= n)

        if len(hand) % groupSize != 0:          # TIME O(1): quick fail
            return False

        freq = {}                               # SPACE O(k): one key per distinct value
        for card in hand:                       # TIME O(n): one pass over all cards
            if card in freq:                    # O(1) average dict check
                freq[card] += 1
            else:
                freq[card] = 1

        pq = []                                 # SPACE O(k): distinct values only
        for card in freq:                       # k pushes
            heapq.heappush(pq, card)            # O(log k) each -> O(k log k) total

        # Each round of the inner for-loop uses up ONE card,
        # so across ALL rounds it runs exactly n times in total.
        while pq:
            start = pq[0]                       # O(1): peek the smallest
            for val in range(start, start + groupSize):
                if val not in freq or freq[val] == 0:   # O(1)
                    return False
                freq[val] -= 1                  # O(1)
                if freq[val] == 0:
                    if val != pq[0]:            # O(1)
                        return False
                    heapq.heappop(pq)           # O(log k), but each value is
                                                # popped only once -> O(k log k) total

        return True

        # TOTAL TIME:  O(n) + O(k log k) + O(n) + O(k log k)
        #            = O(n + k log k)
        #            -> worst case (all distinct, k = n): O(n log n)
        # TOTAL SPACE: freq O(k) + heap O(k) = O(k) -> worst case O(n)


                



