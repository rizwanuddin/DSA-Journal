"""
Allocate Minimum Number of Pages
Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:
    Each student gets at least one book.
    Each book should be allocated to only one student.
    Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1
Examples

Example 1:
Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.
Example 2:
Input Format:
 n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
Result:
 71
Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.


ALLOCATE MINIMUM NUMBER OF PAGES — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array where each element represents the number of pages in a book, and
m students.

I need to allocate all the books to the students in contiguous order,
and every student should receive at least one book.

I need to minimize the maximum number of pages assigned to any student."


2. BRUTE FORCE

"The straightforward approach would be to try every possible maximum
page limit and check how many students are required for that limit.

This would work, but trying every possible value can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the answer.

The minimum possible answer is max(arr), because one student must be
able to take the largest book.

The maximum possible answer is sum(arr), which represents one student
taking all the books.

So I'll binary search between these two values."


4. KEY OBSERVATION

"The key observation is that for every mid, I'm treating mid as the
maximum number of pages one student is allowed to receive.

I go through the books in order and keep adding pages to the current
student.

If adding another book would make the student's pages greater than mid,
I give that book to a new student.

This tells me how many students are required for that page limit.

If I can allocate the books using m students or fewer, mid works, so
I'll search left for a smaller maximum.

If I need more than m students, mid is too small, so I'll search right
for a larger maximum."


5. APPROACH

"I'll first check whether there are more students than books. If so,
the allocation is impossible, so I'll return -1.

Then I'll set low to max(arr) and high to sum(arr).

For each mid, I'll treat mid as the maximum pages allowed for one
student.

I'll start with one student and a page sum of zero.

I'll go through the books in order.

If the current book fits within mid, I'll add it to the current
student's pages.

Otherwise, I'll increase the student count and give the current book
to the new student.

After processing all the books, if student <= m, mid is possible, so
I'll save it and search left for a smaller answer.

Otherwise, I'll search right for a larger page limit."


6. WHILE CODING

"I'm setting low to max(arr) because the largest book must fit with
at least one student.

I'm setting high to sum(arr) because that's the maximum possible answer.

For each mid, I'm treating it as the maximum pages one student can
receive.

I'm starting student at 1 because I begin by assigning books to the
first student.

If pages_sum + pages <= mid, the current student can take this book,
so I'll add it.

Otherwise, I'll move to a new student and make the current book the
first book assigned to that student.

If student <= m, this page limit works, so I'll search left to minimize
it.

If student > m, I need a larger page limit, so I'll search right."


7. EDGE CASES

"If there are more students than books, every student cannot receive
at least one book, so I'll return -1."

if m > len(arr):
    return -1

"If the array could be empty, I'll handle that before calling max()
or sum()."

if not arr:
    return -1

"If there is only one student, that student has to receive every book,
so the answer is the total number of pages."

if m == 1:
    return sum(arr)


8. COMPLEXITY

"Let S be the sum of all pages and M be the largest book.

Binary search takes O(log(S - M + 1)) iterations.

For every mid, I traverse all n books to calculate how many students
are required.

So the total time complexity is O(n log(S - M + 1)), commonly written
as O(n log S).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""

class Solution:
    def min_pages(self, arr, m):

        if m > len(arr):
            return -1

        low = max(arr)
        high = sum(arr)
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            student = 1
            pages_sum = 0

            for pages in arr:

                if pages_sum + pages <= mid:
                    pages_sum += pages

                else:
                    student += 1
                    pages_sum = pages

            if student <= m:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans

'''
ALLOCATE MINIMUM PAGES

Goal:
Give books to m students in contiguous order while minimizing the
maximum pages given to any student.

Binary search on MAXIMUM PAGES allowed per student.

low = max(arr)
→ A student must be able to take the largest book.

high = sum(arr)
→ Maximum useful limit is all pages combined.

For every mid:
→ Treat mid as maximum pages one student can receive.
→ Keep adding books to the current student.
→ If adding a book exceeds mid, give that book to a new student.

If students <= m:
→ mid works
→ save mid
→ search LEFT for a smaller maximum.

If students > m:
→ mid is too small
→ search RIGHT for a larger maximum.


DRY RUN:

arr = [12, 34, 67, 90]
m = 2

low = 90
high = 203

mid = 146:
Student 1 → 12 + 34 + 67 = 113
Student 2 → 90
2 students → works ✅ → LEFT

mid = 117:
Student 1 → 113
Student 2 → 90
works ✅ → LEFT

mid = 103:
Student 1 → 12 + 34 = 46
Student 2 → 67
Student 3 → 90
3 students → fails ❌ → RIGHT

Eventually:

112 → fails ❌
113 → works ✅

Answer = 113

MAIN RULE:

students <= m → works → LEFT
students > m  → too small → RIGHT

Time: O(N * log(sum(arr) - max(arr)))
Space: O(1)
'''