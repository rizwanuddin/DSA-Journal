"""
I’m using a hash set approach to find the longest consecutive sequence efficiently. First, I put all the numbers into a set called num_set, which lets me check whether a number exists in 
O(1) average time and also removes duplicates. Then I go through each number in the set, but I only start building a sequence if the current number is actually the beginning of a sequence. 
I know it’s the beginning when num - 1 is not in the set. For example, if I have 1, I check whether 0 exists; if it doesn’t, then 1 must be the start. Once I find a starting number, I keep 
checking whether the next consecutive number, current_num + 1, exists in the set. Every time it does, I move to that number and increase current_length. When the sequence ends, I compare 
its length with longest and keep the larger value. The important optimization is that I only build sequences from their starting number, instead of starting from every element, which 
avoids repeatedly checking the same sequence. For example, with [100, 4, 200, 1, 3, 2], I start from 1 and find 1 → 2 → 3 → 4, giving a longest length of 4. The time complexity is O(n) on 
average because each number is processed as part of a consecutive sequence at most once, and hash-set lookups are O(1) on average. The space complexity is O(n) because I store all the 
numbers in the hash set.
"""
class Solution:
    # Function to find the longest consecutive sequence
    def longest_consecutive(self, nums):

        # Handle empty array
        if not nums:
            return 0

        # Store all numbers in a hash set
        num_set = set(nums)

        # Store the maximum sequence length
        longest = 0

        # Traverse through each number
        for num in num_set:

            # Check if num is the START of a sequence
            # If num - 1 doesn't exist, num must be the start
            if num - 1 not in num_set:

                current_num = num
                current_length = 1

                # Keep checking for the next consecutive number
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update the longest sequence found
                longest = max(longest, current_length)

        return longest


# Main method
nums = [100, 4, 200, 1, 3, 2]

# Create an instance of Solution
finder = Solution()

# Find longest consecutive sequence
result = finder.longest_consecutive(nums)

print("Longest consecutive sequence length:", result)