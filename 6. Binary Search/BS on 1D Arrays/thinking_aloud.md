how to think aloud example for lower bound question-
LOWER BOUND — THINK ALOUD WHILE CODING


"I'm going to create a class called LowerBoundFinder."

class LowerBoundFinder:


"Inside the class, I'll define a method called lower_bound.

It takes the sorted array and x, which is the value whose lower bound
I'm looking for."

    def lower_bound(self, arr, x):


"Since this is a binary search problem, I'm going to initialize low at
the beginning of the array and high at the end of the array."

        low, high = 0, len(arr) - 1


"I'll also initialize ans to len(arr).

The lower bound is the first index where the value is greater than or
equal to x.

If no such element exists, the expected answer is the length of the
array, so len(arr) is a good default value."

        ans = len(arr)


"Now I'll start my binary search.

As long as low is less than or equal to high, I still have elements
left in my search space."

        while low <= high:


"I'll calculate the middle index of my current search space."

            mid = (low + high) // 2


"Now I'll check whether the middle element is greater than or equal to x.

If it is, then this index could potentially be my lower bound."

            if arr[mid] >= x:


"So I'll save mid as my current possible answer."

                ans = mid


"But I specifically want the FIRST index where the value is greater
than or equal to x.

So even though I found a valid answer, there might be another valid
answer further to the left.

Therefore, I'll move high to mid minus one and continue searching
the left half."

                high = mid - 1


"Otherwise, arr[mid] is smaller than x.

That means mid cannot be the lower bound, and because the array is
sorted, nothing to the left of mid can be the lower bound either.

So I'll eliminate the left half and move low to mid plus one."

            else:
                low = mid + 1


"Once low becomes greater than high, my search is finished.

At this point, ans contains the leftmost index where the value is
greater than or equal to x.

So I'll return ans."

        return ans


"Now outside the class, I'll create my sorted input array."

arr = [3, 5, 8, 15, 19]


"I'll set x to 9.

So I'm looking for the first element that is greater than or equal
to 9."

x = 9


"Now I'll create an object of my LowerBoundFinder class."

finder = LowerBoundFinder()


"I'll call the lower_bound method using my array and x, and store
the returned index in ind."

ind = finder.lower_bound(arr, x)


"Finally, I'll print the result."

print("The lower bound is the index:", ind)