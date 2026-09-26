"""
Best Time to Buy And Sell Stock - Explanation

You are given an integer array prices where prices[i] is the price 
of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a 
different day in the future to sell it.Return the maximum profit 
you can achieve. You may choose to not make any transactions, in 
which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0



## Best Time to Buy and Sell Stock

**Clarify:**
- Pick one day to buy, a later day to sell
- Return max possible profit, or 0 if no profitable transaction exists

**Brute force:**
- Check every pair of buy/sell days, track max profit
- O(n²) time, O(1) space

**Optimize:**
- Single pass, track the lowest price seen so far and the best profit possible so far
- O(n) time

**Key observation:**
- Profit only depends on the cheapest buy point BEFORE the current day — you never need to look at all previous days again, just the running minimum
- As you scan forward, either today is a new lowest price (update buy point), or today is a chance to sell for a new best profit

**Approach:**
- min_price = infinity, max_profit = 0
- for each price:
  - if price < min_price: update min_price
  - else: check if price - min_price beats max_profit, update if so

**While coding:**
- min_price starts at infinity so the very first price always becomes the initial buy point
- max_profit starts at 0, matching the "no transaction" fallback

**Edge cases:**
- Array with 1 price → no valid sell day, profit stays 0
- Strictly decreasing prices → profit stays 0, never worth selling

**Complexity:**
- Time: O(n) — one pass
- Space: O(1) — two variables
"""
class Solution:
    def buy_sell(self, prices):
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
            