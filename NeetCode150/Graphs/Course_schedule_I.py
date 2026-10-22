"""
Course Schedule I - Medium

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if 
you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is 
impossible.





# Course Schedule: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I have numCourses courses, labeled 0 to numCourses - 1.
I'm given a list of prerequisite pairs.
A pair [a, b] means I have to take course b before course a.
I need to return True if it's possible to finish every course,
and False if it's not."

"I have a few quick questions before I start."

"Just to confirm, does [a, b] mean b comes before a, and not the other way around?"
→ I'll assume b comes before a.

"Can a course have no prerequisites at all?"
→ I'll assume yes.

"Can the prerequisite list be empty?"
→ I'll assume yes, and then I can take every course, so it's True.

"Can there be duplicate pairs, or a course that lists itself?"
→ I'll assume it can happen, and I'll handle it.

"Okay, so if I think of courses as nodes and prerequisites as arrows,
the only thing that can stop me is a cycle.
For example, A needs B, and B needs A.
So the real question is: does this graph have a cycle?"

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
numCourses = 2, prerequisites = [[1, 0]]
```
"Course 1 needs course 0. I take 0, then 1. Answer: True."

```
numCourses = 2, prerequisites = [[1, 0], [0, 1]]
```
"Course 1 needs 0, and 0 needs 1. That's a cycle. Answer: False."

```
numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
```
"Course 3 needs 1 and 2, and both of those need 0.
Course 0 is shared, but there's no cycle. Answer: True."

"A few edge cases:"
- "No prerequisites: every course is free to take. Answer: True."
- "A course that needs itself, like [0, 0]: that's a cycle. Answer: False."
- "Courses that aren't in any pair: they don't block anything."
- "A long chain like 0 → 1 → 2 → 3 with no loop back: Answer: True."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
For each course, I follow its prerequisites, then their prerequisites,
and so on, keeping track of the path I'm on.
If I ever come back to a course that's already on my current path,
I've found a cycle, so I return False."

"This works because a cycle is exactly a path that loops back on itself,
and I'm checking from every course."

"The time is at least O(V * (V + E)),
where V is the number of courses and E is the number of pairs.
Each course starts its own full search,
and one search can walk the whole graph."

"It can actually get even worse.
If many courses share the same prerequisites,
I re-explore those shared chains again through every path that reaches them."

"The space is O(V + E), for the graph and the path."

"The problem is that I keep re-checking courses
I already proved are fine.
Once I know a course has no cycle below it,
I should never have to check it again."

## 4. Optimal solution

"The bottleneck is re-checking the same courses over and over.
So I want to remember the answer for each course once I know it."

"Instead of starting a fresh search from every course,
I can run DFS and give each course one of three states."

"First, not visited yet.
Second, visiting, which means it's on my current path right now.
Third, done, which means I've fully checked it and found no cycle below it."

"The data structures I'll use are an adjacency list and two sets.
The adjacency list maps each course to its prerequisites,
so I can find them directly.
The visiting set holds the courses on my current path,
because if I see one of those again, I've looped back, so it's a cycle.
The done set holds courses that are already proven safe,
because I can skip them right away next time."

"As I go through each course, I run DFS on it."

"When I reach a course that's in visiting, I return False,
because that means there's a cycle."

"When I reach a course that's in done, I return True,
because I already checked it."

"Otherwise, I add it to visiting, and check all of its prerequisites.
If any of them returns False, I return False right away."

"When all of its prerequisites are fine,
I take it out of visiting, put it in done, and return True."

"At the end, if no course found a cycle, I return True."

"The time is O(V + E).
Each course is fully processed only once, because of the done set,
and each prerequisite pair is looked at once."

"The space is O(V + E).
The adjacency list stores every pair,
the two sets hold up to V courses,
and the call stack can go V deep."

"So I go from at least O(V * (V + E)) down to O(V + E)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called course_Schedule
that takes self, numCourses, and prerequisites."

"I'll start by building the graph.
I'll create an empty dictionary called adj.
It maps each course to the list of courses it depends on."

"Then I loop over each pair, unpacking it into k and v.
k is the course, and v is its prerequisite."

"If k isn't in adj yet, I give it an empty list.
Then I append v to adj[k]."

"I only add courses that actually have prerequisites.
Courses with none just won't be in the dictionary,
and I'll handle that when I look them up."

"Next, I'll create an empty set called visiting.
It holds the courses on my current DFS path."

"And an empty set called done.
It holds courses I've fully checked and know are safe."

"Now I'll define a helper called dfs that takes a course i.
It returns True if there's no cycle starting from i,
and False if there is one."

"First thing inside it, I check if i is in visiting.
If it is, I've come back to a course that's still on my current path.
That's a cycle, so I return False."

"Then I check if i is in done.
If it is, I already proved this course is safe, so I return True right away.
This is what stops me from repeating work."

"If neither is true, this is a new course.
I add i to visiting, because it's now on my current path."

"Then I loop over each prereq in adj.get(i, []).
I'm using get with an empty list as the default,
so a course with no prerequisites just skips the loop
instead of crashing."

"For each prereq, I call dfs on it and store the result.
If the result is False, there's a cycle somewhere below,
so I return False right away."

"If the loop finishes, every prerequisite is safe.
So I remove i from visiting, because I'm leaving this path.
And I add i to done, so I never have to check it again.
Then I return True."

"Now I loop over every course from 0 to numCourses - 1.
I loop over all of them, not just the ones in the pairs,
because the graph can have several separate parts."

"For each course, I call dfs and store the result.
If it's False, I found a cycle, so I return False."

"If the loop finishes, no course found a cycle,
so I return True."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[[1, 0]]: dfs(0) has no prereqs, so 0 goes to done.
  dfs(1) adds 1 to visiting, checks 0, which is done, so it's safe.
  1 goes to done. The answer is True, which matches."
- "[[1, 0], [0, 1]]: dfs(0) adds 0 to visiting, then goes to 1.
  dfs(1) adds 1 to visiting, then goes back to 0.
  0 is in visiting, so that's a cycle. The answer is False, which matches."
- "Shared prerequisite: dfs(0) finishes first and goes to done.
  When 1 and 2 reach 0 later, it's already in done, so they return True right away.
  Then 3 reaches 1 and 2, which are both done. The answer is True."
- "No prerequisites: adj is empty, every course returns True. The answer is True."
- "[0, 0]: dfs(0) adds 0 to visiting, then its prereq is 0,
  which is in visiting. The answer is False."

"The output matches what I expected for all of them."

"To recap, time is O(V + E) and space is O(V + E)."

"If the chain of courses could be very long,
the recursion might hit Python's limit of about 1000.
In that case, I'd use Kahn's algorithm instead.
That's BFS with in-degree counts:
I keep taking courses that have no remaining prerequisites,
and if I can't take all of them, there's a cycle."
"""

class Solution:
    def course_Schedule(self, numCourses, prerequisites):
        adj = {}
        for k, v in prerequisites:
            if k not in adj:
                adj[k] = []
            adj[k].append(v)

        visiting = set()
        done = set()

        def dfs(i):
            if i in visiting:
                return False
            if i in done:
                return True

            visiting.add(i)
            for prereq in adj.get(i, []):
                result = dfs(prereq)
                if result == False:
                    return False
            visiting.remove(i)
            done.add(i)
            return True

        for course in range(numCourses):
            result = dfs(course)
            if result == False:
                return False

        return True
