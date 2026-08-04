"""
Linear Search
Time Complexity : O(n)
Space Complexity : O(1)
"""
def find_max_consecutive_ones(arr):
    # Stores current consecutive 1's count
    count = 0

    # Stores maximum consecutive 1's found
    max_count = 0

    # Traverse the array
    for num in arr:

        # If current element is 1, increase count
        if num == 1:
            count += 1

        # If current element is 0, reset count
        else:
            count = 0

        # Update the maximum count
        max_count = max(max_count, count)

    # Return the maximum consecutive 1's
    return max_count


# Driver Code
arr = [1, 1, 0, 1, 1, 1]

answer = find_max_consecutive_ones(arr)

print("The maximum consecutive 1's are", answer)

"""
Also if you are coming from java/C++ background
you can also do this by the indexing way
instead of using "for num in arr:"
"""
def find_max_consecutive_ones(arr):
    # Stores current consecutive 1's count
    count = 0

    # Stores maximum consecutive 1's found
    max_count = 0

    # Traverse the array using indices
    for i in range(len(arr)):

        # If current element is 1, increase count
        if arr[i] == 1:
            count += 1

        # If current element is 0, reset count
        else:
            count = 0

        # Update the maximum count
        max_count = max(max_count, count)

    # Return the maximum consecutive 1's
    return max_count


# Driver Code
arr = [1, 1, 0, 1, 1, 1]

answer = find_max_consecutive_ones(arr)

print("The maximum consecutive 1's are", answer)