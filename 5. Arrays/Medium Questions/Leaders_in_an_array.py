"""
I’m using a right-to-left traversal to find all the leaders in the array. A leader is an element that is greater than every element to its right. Since the last element has nothing to its 
right, it is always considered a leader, so I start by adding it to the leaders list and storing it as max_so_far. Then I traverse the array from right to left, and for each element I 
compare it with max_so_far, which represents the largest value I’ve seen to its right. If arr[i] > max_so_far, then I know the current element is greater than everything to its right, so 
it is a leader. I update max_so_far to the current element and add it to the leaders list. Since I’m finding the leaders from right to left, they are initially stored in reverse order, so 
at the end I reverse the leaders list to return them in their original left-to-right order. For example, in [10, 22, 12, 3, 0, 6], the leaders are [22, 12, 6]. The time complexity is O(n) 
because I traverse the array once and reverse the result once, which is still O(n), and the space complexity is O(n) in the worst case because every element could be a leader and therefore 
stored in the output list.
"""
class Solution:
    # Function to find the leaders in an array
    def leaders(self, arr):

        # Handle empty array
        if not arr:
            return []

        # List to store all the leaders
        leaders = []

        # The last element is always a leader
        max_so_far = arr[-1]
        leaders.append(max_so_far)

        # Traverse the array from right to left
        for i in range(len(arr) - 2, -1, -1):

            # If current element is greater than
            # every element seen on its right
            if arr[i] > max_so_far:

                # Update the maximum element seen so far
                max_so_far = arr[i]

                # Add the new leader to the list
                leaders.append(arr[i])

        # Since we found leaders from right to left,
        # reverse them to restore original order
        leaders.reverse()

        # Return the final list of leaders
        return leaders


# Main method
arr = [10, 22, 12, 3, 0, 6]

# Create an instance of the Solution class
finder = Solution()

# Find the leaders
leaders = finder.leaders(arr)

# Print the leaders
print("Leaders in the array are: ", end="")

for leader in leaders:
    print(leader, end=" ")

print()