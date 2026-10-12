"""
Median of Two Sorted Arrays - Explanation

You are given two integer arrays nums1 and nums2 of size m and n 
respectively, where each is sorted in ascending order. Return the 
median 
value among all elements of the two arrays.
Your solution should run in O(log(m+n))
O(log(m+n)) time.

Example 1:
Input: nums1 = [1,2], nums2 = [3]
Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:
Input: nums1 = [1,3], nums2 = [2,4]
Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.




## Median of Two Sorted Arrays

**Clarify:**
- so I'm given two sorted arrays, and I need to find the median if I were to merge them
- if the total count is odd, median is just the middle value, if it's even, it's the average of the two middle values
- and I shouldn't actually merge them, that would be too slow, they probably want something faster

**Brute force:**
- the easy way is just merge both arrays into one sorted array, then grab the middle value or average the two middle values
- that's O(m+n) time, works but there's a faster way using binary search

**Optimize:**
- since both arrays are already sorted, I can binary search on how many elements to take from the smaller array, and figure out the rest from the bigger one
- that gets me down to O(log(min(m,n))) time, which is way better

**Key observation:**
- the whole idea is I'm trying to make an imaginary cut in both arrays, so that everything on the left side of both cuts combined is less than or equal to everything on the right side
- if I decide how many elements come from array one, that automatically tells me how many need to come from array two, since I know exactly how big the left half should be
- so I just need to check, is the last element on the left side of array one less than or equal to the first element on the right side of array two, and the same the other way around for array two and array one
- if both of those checks pass, I've found the correct cut, and I don't even need to merge anything to get the answer

**Approach:**
- always binary search the smaller array, so the search space stays small
- figure out how many total elements should be on the left side, that's just half of the combined length, rounded up
- binary search cut1, which is how many elements I take from array one, and cut2 is just whatever's left needed from array two
- look at the values right around each cut, using negative infinity or positive infinity for edges that go out of bounds
- if the cut is valid, calculate the median based on whether the total count is odd or even
- if not valid, shift the binary search left or right depending on which side was too big

**While coding:**
- first I define the class Solution
- then the function find_median, taking arr1 and arr2
- first thing I do is check if arr1 is bigger than arr2, if it is, I just call the same function again but swapped, so I always binary search the smaller one
- I get n1 and n2 as the lengths of both arrays
- I set low to 0 and high to n1
- I calculate left_size, which is how many elements the combined left side should have, that's n1 plus n2 plus 1, divided by 2
- I start a while loop that runs while low is less than or equal to high
- inside, I calculate cut1 as low plus high divided by 2
- then cut2 is just left_size minus cut1
- now I figure out left1 and right1 from array one — if cut1 is 0, left1 is negative infinity since there's nothing to the left, otherwise it's arr1 at cut1 minus 1, and if cut1 equals n1, right1 is positive infinity since there's nothing to the right, otherwise it's arr1 at cut1
- I do the exact same thing for left2 and right2, but using array two and cut2
- then I check if left1 is less than or equal to right2, and left2 is less than or equal to right1
- if both are true, this is the correct cut, so now I check if the total length is odd, if yes I return the max of left1 and left2
- if the total length is even, I take the max of left1 and left2 as left_max, and the min of right1 and right2 as right_min, and return the average of those two
- if left1 is bigger than right2, that means I took too many from array one, so I bring high down to cut1 minus 1
- otherwise, I took too few from array one, so I push low up to cut1 plus 1

**Edge cases:**
- if one array is empty, the cut logic should still work since infinity handles the missing side
- if both arrays are the same size, nothing special happens, the swap check just doesn't trigger
- if there's only one element total across both arrays, the loop should resolve that immediately

**Complexity:**
- time is O(log(min(m,n))), since I'm only binary searching the smaller array
- space is O(1), not counting the recursion call for swapping, which happens at most once



Always binary search the smaller array, not the bigger one
Once you pick how many elements to take from it, the other array’s cut is forced — cut2 = left_size - cut1
If you searched the bigger array instead, that forced cut on the smaller array could go negative or past its actual length — breaks completely
Searching the smaller one keeps the forced cut mathematically guaranteed to stay in bounds

"""
class Solution:
    def FindMedian(self, arr1, arr2):
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 > len2:
            return self.FindMedian(arr2, arr1)
        low = 0
        high = len1
        left_size = (len1 + len2 + 1) // 2
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = left_size - cut1
            if cut1 == 0:
                left1 = float("-inf")
            else:
                left1 = arr1[cut1 - 1]
            if cut1 == len1:
                right1 = float("inf")
            else:
                right1 = arr1[cut1]

            if cut2 == 0:
                left2 = float("-inf")
            else:
                left2 = arr2[cut2 - 1]
            if cut2 == len2:
                right2 = float("inf")
            else:
                right2 = arr2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (len1 + len2) % 2 == 1:
                    return max(left1, left2)
                else:
                    left_max = max(left1, left2)
                    right_max = min(right1, right2)
                    return (left_max + right_max) / 2
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
