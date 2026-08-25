"""
I’m using a single-pass greedy approach to find the maximum profit from buying and selling a stock once. The main idea is that as I go through the prices, I keep track of the lowest price 
I’ve seen so far using min_price, because I always want to buy as cheaply as possible. For each price, if it is smaller than min_price, I update min_price because this would be a better 
day to buy. Otherwise, I calculate the profit I would make if I sold at the current price using price - min_price, and I compare that with max_profit to keep the best profit I’ve found so 
far. This automatically makes sure that I buy before I sell, because min_price only contains prices from the current day or previous days. If the prices only decrease, max_profit stays 0, 
meaning no profitable transaction is possible. The time complexity is O(n) because I go through the prices only once, and the space complexity is O(1) because I only use min_price and 
max_profit.
"""
class ArrayManipulator:
    def rearrange_by_sign(self, A):
        n = len(A)
        ans = [0] * n  # Initialize result array with zeros

        pos_index = 0  # Even indices for positive numbers
        neg_index = 1  # Odd indices for negative numbers

        for i in range(n):
            if A[i] < 0:
                # Place negative at odd index
                ans[neg_index] = A[i]
                neg_index += 2
            else:
                # Place positive at even index
                ans[pos_index] = A[i]
                pos_index += 2

        return ans

# Main execution
if __name__ == "__main__":
    A = [1, 2, -4, -5]
    obj = ArrayManipulator()
    result = obj.rearrange_by_sign(A)
    print(" ".join(map(str, result)))
