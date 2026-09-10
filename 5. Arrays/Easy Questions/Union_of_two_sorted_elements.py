"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of 
two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.

’m using a two-pointer approach because both arrays are already sorted. I keep i at the start of 
arr1 and j at the start of arr2. I compare arr1[i] and arr2[j]. If the value in arr1 is smaller, 
I add it to the result and move i forward. If the value in arr2 is smaller, I add it and move j 
forward. If both values are the same, I add it only once and move both pointers forward. Before 
adding anything, I check Union[-1] != value so I don’t add duplicates. When one array finishes, 
I add the remaining elements from the other array while still avoiding duplicates. The time 
complexity is O(n + m) because I go through both arrays once, and the extra space is O(1) if we 
don’t count the output list; the output itself can take O(n + m) space.
"""

class Solution:
    # Function to find union of two sorted arrays using two pointers
    def findUnion(self, arr1, arr2, n, m):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)


