"""
I’m using a single-pass greedy approach to find the maximum profit from buying and selling a stock once. The main idea is that as I go through 
the prices, I keep track of the lowest price I’ve seen so far using min_price, because I always want to buy as cheaply as possible. For each 
price, if it is smaller than min_price, I update min_price because this would be a better day to buy. Otherwise, I calculate the profit I 
would make if I sold at the current price using price - min_price, and I compare that with max_profit to keep the best profit I’ve found so 
far. This automatically makes sure that I buy before I sell, because min_price only contains prices from the current day or previous days. If 
the prices only decrease, max_profit stays 0, meaning no profitable transaction is possible. The time complexity is O(n) because I go through 
the prices only once, and the space complexity is O(1) because I only use min_price and max_profit.
"""
class Solution:
    # Function to calculate maximum profit using single pass
    def stockbuySell(self, prices):
        # Initialize the minimum price to a large number
        min_price = float('inf')

        # Initialize the maximum profit to 0
        max_profit = 0

        # Traverse each price in the array
        for price in prices:
            # If current price is less than min_price, update min_price
            if price < min_price:
                min_price = price
            # Else calculate profit and update max_profit if it's greater
            else:
                max_profit = max(max_profit, price - min_price)

        # Return the maximum profit found
        return max_profit
