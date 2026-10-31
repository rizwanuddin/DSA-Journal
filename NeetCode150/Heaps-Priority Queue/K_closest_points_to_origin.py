"""
K Closest Points to Origin - Medium

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are 
returned.)

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is 
sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted




# K Closest Points to Origin: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a list of points, where each point is [x, y],
and a number k.
I need to return the k points that are closest to the origin, (0, 0).
Distance is the regular straight-line distance."

"I have a few quick questions before I start."

"Can I return the points in any order?"
→ I'll assume yes.

"Is k always between 1 and the number of points?"
→ I'll assume yes.

"Can the coordinates be negative?"
→ I'll assume yes. Squaring takes care of that.

"Can two points be the same distance away?"
→ I'll assume the answer is still unique, like the problem says,
so I don't need a special tie rule.

"Do I need the actual distance, or just which points are closest?"
→ I'll assume just which points.
So I can compare x² + y² and skip the square root.

"Okay, so I need the k points with the smallest x² + y²."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
points = [[0,2], [2,2]], k = 1
```
"(0,2) has a squared distance of 4, and (2,2) has 8.
Answer: [[0,2]]."

```
points = [[0,2], [2,0], [2,2]], k = 2
```
"(0,2) is 4, (2,0) is 4, and (2,2) is 8.
Answer: [[0,2], [2,0]], in any order."

"A few edge cases:"
- "k equals the number of points: return all of them."
- "One point and k = 1: return that point."
- "Negative coordinates, like [-3, 4]: the squared distance is 25."
- "A point at the origin, [0, 0]: its distance is 0, so it's always included."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I compute the distance for every point,
sort all the points by distance,
and return the first k."

"This works because after sorting,
the closest points are right at the front."

"The time is O(n log n), because of the sort."

"The space is O(n), for the list of points with their distances."

"The problem is that I'm putting all n points in perfect order,
when I only need the first k.
Everything after the first k doesn't need to be sorted."

## 4. Optimal solution

"The bottleneck is sorting all the points when I only need the k smallest."

"Instead of fully sorting everything,
I can put all the points in a min-heap,
and only pull out the k smallest."

"The data structure I'll use is a min-heap keyed by squared distance,
because it gives me the closest remaining point each time I pop,
without sorting the rest."

"As I go through the points, I compute x² + y² for each one,
and store it with the point as a tuple, (distance, x, y)."

"Then I heapify the whole list at once.
That builds the heap from the bottom up in O(n),
which is faster than pushing one point at a time."

"When the heap is built, I pop k times.
Each pop gives me the next closest point."

"At the end, I return the k points I popped."

"The time is O(n + k log n).
Building the list is O(n), heapify is O(n),
and each of the k pops is O(log n)."

"The space is O(n), because the heap holds every point."

"So I go from O(n log n) down to O(n + k log n),
which is close to O(n) when k is small."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import heapq.
In Python, it gives me a min-heap on a regular list."

"Then I'll make a class called Solution,
and a function called Kclosest that takes self, points, and k."

"I'll start with an empty list called heap.
Right now it's just a list. I'll turn it into a heap after I fill it."

"Then I loop over each point, unpacking it into x and y."

"For each one, I compute dist as x * x + y * y.
That's the squared distance.
I skip the square root, because if one distance is smaller,
its square is smaller too, so the order is the same.
It's also faster, and I avoid floating-point numbers."

"Then I append the tuple (dist, x, y) to the list.
I put dist first, because Python compares tuples by the first item,
so the heap will order the points by distance.
I keep x and y so I know which point it was."

"After the loop, I call heapq.heapify on the list.
That turns it into a valid min-heap in O(n),
with the closest point at the top."

"Next, I create an empty list called result.
This holds the answer."

"Then I loop k times."

"Each time, I pop from the heap,
and unpack it into dist, x, and y.
heappop always gives me the closest point that's left,
and the heap fixes itself in O(log n)."

"Then I append [x, y] to result.
I leave out the distance, because the answer only needs the point."

"After k pops, I return result."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[[0,2], [2,2]], k = 1: the list is (4,0,2) and (8,2,2).
  After heapify, (4,0,2) is on top.
  I pop once and get [0,2]. The answer is [[0,2]], which matches."
- "[[0,2], [2,0], [2,2]], k = 2: the list is (4,0,2), (4,2,0), and (8,2,2).
  I pop (4,0,2), then (4,2,0).
  The answer is [[0,2], [2,0]], which matches."
- "k equals the number of points: I pop everything,
  so every point gets returned."
- "One point and k = 1: one pop, and I return it."
- "[-3, 4]: dist is 9 + 16 = 25, so the negative number is handled by squaring."
- "[0, 0]: dist is 0, so it's always the first one popped."

"The output matches what I expected for all of them."

"To recap, time is O(n + k log n) and space is O(n)."

"If memory matters, or the points are coming in as a stream,
I'd keep a max-heap of size k instead.
I push each point as (-dist, x, y),
and pop the farthest one whenever the heap gets bigger than k.
That's O(n log k) time and only O(k) space.
And if they want the best average time,
Quickselect gets O(n) on average, but it's O(n²) in the worst case."
"""
import heapq
class Solution():
    def Kclosest(self, points, k):
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heap.append((dist, x, y))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result

