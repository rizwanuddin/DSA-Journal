"""
METHOD 1 OPTIMAL APPROACH - Hashing

Two Sum : Check if a pair with given sum exists in Array
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

I’m using a hash map approach to solve the Two Sum problem efficiently. The main idea is that for every number num, I calculate the value 
I would need to reach the target using complement = target - num. As I iterate through the array, I use the dictionary mp to store the 
numbers I’ve already seen along with their indices. For each current number, I first check whether its complement already exists in the 
hash map. If it does, then I know those two numbers add up to the target. In the first variant, I only need to know whether a pair 
exists, so I immediately return "YES" when I find one and "NO" if I finish the loop without finding one. In the second variant, the logic 
is the same, but instead of returning "YES", I return the index stored for the complement and the current index as [mp[complement], i]. 
An important detail is that I check for the complement before storing the current number, which prevents accidentally using the same 
array element twice. For example, with target = 14, when I reach 8, I calculate 14 - 8 = 6, see that 6 was already stored, and know that 
6 + 8 = 14. The time complexity is O(n) on average because I traverse the array once and hash map lookups are O(1) on average, while the 
space complexity is O(n) because in the worst case I may store every element in the hash map.
"""

class Solution:
    # Variant 1: Check if two numbers sum to target using hashing
    def two_sum_exists(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        # Iterate over all elements
        for i, num in enumerate(arr):
            complement = target - num
            # Check if complement exists in dictionary
            if complement in mp:
                return "YES"  # Pair found
            # Store current element and its index
            mp[num] = i
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target using hashing
    def two_sum_indices(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(arr):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))


"""
METHOD 2 BETTER APPROACH - TWO POINTER

I’m using a two-pointer approach, but since two pointers work based on the ordering of values, I first need to sort the array. 
Because the second variant needs to return the original indices, I create nums_with_index, which stores each number together with its 
original index, and then I sort these pairs based on the number. After sorting, I place left at the smallest value and right at the 
largest value. In each iteration, I calculate current_sum by adding the values at the two pointers. If current_sum == target, I’ve found 
the required pair, so in the first variant I return "YES", while in the second variant I return their original indices using the indices 
saved in the tuples. If current_sum < target, the sum is too small, so I move left one position to the right to get a larger value and 
potentially increase the sum. If current_sum > target, the sum is too large, so I move right one position to the left to get a smaller 
value and decrease the sum. I continue until the pointers meet, and if no pair is found, I return "NO" or [-1, -1]. For example, with a 
target of 14, the algorithm eventually finds 6 + 8 = 14 and can return their original indices [1, 3]. The time complexity is O(n log n) 
because sorting takes O(n log n), while the two-pointer traversal itself takes O(n). The space complexity is O(n) in this implementation 
because I create a separate nums_with_index list containing all the values and their original indices.
"""
class Solution:
    # Variant 1: Check if two numbers sum to target using two-pointer approach
    def two_sum_exists(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort list based on the values (to apply two-pointer technique)
        nums_with_index.sort(key=lambda x: x[0])

        # Initialize two pointers: left at start, right at end
        left, right = 0, len(arr) - 1
        
        # Continue until pointers cross
        while left < right:
            # Calculate sum of values at pointers
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                # Found a pair
                return "YES"
            elif current_sum < target:
                # Sum too small, move left pointer to right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer to left to decrease sum
                right -= 1
        
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target
    def two_sum_indices(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort the list by values
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                # Return original indices of found elements
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                # Move left pointer right to increase sum
                left += 1
            else:
                # Move right pointer left to decrease sum
                right -= 1
        
        # No valid pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))  # Output: YES
    print(sol.two_sum_indices(arr, target)) # Output: [1, 3]
