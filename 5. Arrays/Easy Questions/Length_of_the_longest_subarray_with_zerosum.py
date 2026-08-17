"""
Problem Statement: Given an array containing both positive and negative integers, we have to find the
                   length of the longest subarray with the sum of all elements equal to zero. 
                
I’m using a prefix sum and hash map approach because the array can contain both positive and negative numbers, 
which makes a normal sliding window unreliable. As I iterate through the array, I keep a running prefix sum s, 
which represents the sum from index 0 to the current index. The main idea is that if I see the same prefix sum 
twice, then the elements between those two positions must add up to 0, because subtracting two equal prefix 
sums gives zero. I use the hash map mpp to store each prefix sum along with the first index where it appeared. 
If s becomes 0, that means the entire subarray from index 0 to i has sum zero, so its length is i + 1. 
Otherwise, if s already exists in the hash map, I know there is a zero-sum subarray between the previous 
index and the current index, so I calculate its length using i - mpp[s] and update maxi if it's longer. 
If the prefix sum hasn't been seen before, I store its current index, and I specifically keep the first 
occurrence because the earliest index gives me the longest possible subarray later. The time complexity is 
O(n) because I traverse the array once and hash map operations are O(1) on average, and the space complexity 
is O(n) because, in the worst case, I may store a different prefix sum for every element in the array.
"""

# compute length of the longest subarray with sum 0
def maxLen(A: list[int], n: int) -> int:
    # map prefix sum -> first index seen
    mpp: dict[int, int] = {}
    # best length so far
    maxi = 0
    # running prefix sum
    s = 0

    # iterate over the array
    for i in range(n):
        # update running sum
        s += A[i]

        # if sum is zero, subarray [0..i] has zero sum
        if s == 0:
            # update best length
            maxi = i + 1
        # otherwise check if this sum was seen before
        else:
            # when seen, zero-sum segment between previous index + 1 and i
            if s in mpp:
                # maximize length
                maxi = max(maxi, i - mpp[s])
            # first time seeing this sum
            else:
                # record index
                mpp[s] = i

    # return best length
    return maxi

# program entry
def main():
    # sample input
    A = [9, -3, 3, -1, 6, -5]
    # compute size
    n = len(A)
    # print result
    print(maxLen(A, n))

# run main
if __name__ == "__main__":
    main()
