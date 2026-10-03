"""
Koko Eating Bananas - Explanation

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an 
integer h, which represents the number of hours you have to eat all the bananas. You may decide your bananas-per-hour
 eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has 
 less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour. Return 
 the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 
10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25



## Koko Eating Bananas

**Clarify:**
- Koko eats bananas from piles, one pile at a time, at some fixed speed k bananas per hour
- if a pile has less than k bananas, she still takes a full hour on it, doesn't move to the next pile early
- need to find the minimum k so she finishes all piles within h hours

**Brute force:**
- just try every possible speed starting from 1 upward, check how many hours it takes, stop at the first one that works
- that's slow, could be O(max(piles) times n) in the worst case

**Optimize:**
- this is actually binary search, but not on the array, binary search on the ANSWER itself, meaning the possible eating speeds
- as speed goes up, hours needed goes down, that's a monotonic relationship, which is exactly what makes binary search work here
- so I binary search between speed 1 and max(piles), trying to find the smallest speed that still finishes in time

**Key observation:**
- for any guessed speed mid, I can calculate exactly how many hours it would take using ceil(pile divided by mid) for every pile, then summing them up
- if total hours needed is less than or equal to h, that speed works, so I try to go even slower, meaning I bring high down
- if total hours needed is more than h, that speed is too slow, so I need to go faster, meaning I push low up
- I keep track of the best valid answer I've found so far in a separate variable, since the loop doesn't stop exactly at the answer like normal binary search does

**Approach:**
- low starts at 1, high starts at max(piles), since eating faster than the biggest pile doesn't help further
- loop while low is less than or equal to high
- guess a speed mid, calculate total hours needed at that speed
- if total hours is within the limit, this speed works, save it as a possible answer, then try an even smaller speed
- if total hours is too much, this speed isn't enough, try a bigger speed
- return the best valid speed found

**While coding:**
- first I import ceil from the math module, since banana piles need rounding up, not regular division
- I define the function koko_eating, taking piles and h
- I set low to 1, high to max(piles), and ans to high as a starting fallback
- I start a while loop that runs while low is less than or equal to high
- inside, I calculate mid as low plus high divided by 2
- I set total_hours to 0, then loop through every pile, adding ceil of pile divided by mid to total_hours
- after the loop, I check if total_hours is greater than or equal to h, wait, actually I check if total_hours meets the requirement — if total_hours is greater than or equal to h means it's taking too long or just enough, so I bring high down to mid minus 1 and save mid as my current answer
- otherwise, if total_hours is less than h, meaning it finished early, so I push low up to mid plus 1, trying a slower speed next
- once the loop ends, I return ans

**Edge cases:**
- if there's just one pile, it should still work the same way
- if h is very large, even the slowest speed of 1 might be enough
- if h is very small, almost equal to the number of piles, the speed basically has to be close to max(piles)

**Complexity:**
- time is O(n log(max(piles))), since for every guessed speed in the binary search, I'm looping through all n piles to calculate total hours
- space is O(1), just a few variables being tracked
"""
from math import ceil
class Solution:
    def koko_eating(self, piles, h):
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile/mid)
            if total_hours >= h:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
    