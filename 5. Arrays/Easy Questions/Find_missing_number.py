"""
First Method [Naive Approach] Linear Search
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def missingNum(arr): # arr = [1, 2, 3, 4, 6, 7, 8] 5 not here 
    n = len(arr) + 1 # n = 7 + 1 = 8 (n is what the original length should have been without the missing number)

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1): # (1,9) so i = 1-8.....i is value/the number
        found = False
        for j in range(n - 1): #(0,7) so j = 0-6.....j is index of array
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))


"""
Second Method [Better Approach] Using Hashing (Frequency array hashing)
Time Complexity : O(n)
Space Complexity : O(n)
"""

def missing_number(arr): # arr = [1, 2, 3, 4, 6, 7, 8] 5 not here
    n = len(arr) + 1     # n = 7 + 1 = 8 (n is what the original length should have been without the missing number)

    # Create hash array of size n+1
    hash = [0] * (n + 1) # made array of index 0-8

    # Store frequencies of elements
    for i in range(n-1): # (0,7) so i = 0 - 6
        hash[arr[i]] += 1

    # Find the missing number
    for i in range(1,n+1): # (1,9) so i = 1 - 8
        if hash[i] == 0 :
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res)

"""
Third Method [Expected Approach] Using Sum of n terms formula 
Time Complexity : O(n)
Space Complexity : O(1)
"""
def missing_number(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expSum = n * (n + 1) // 2

    # Return the missing number
    return expSum - totalSum

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))