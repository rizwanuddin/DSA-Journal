"""
Course Schedule II - Medium

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if 
you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of 
them. If it's not possible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []
Explanation: It's impossible to finish all courses.






# Course Schedule II: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I have numCourses courses, labeled 0 to numCourses - 1.
I'm given prerequisite pairs, where [a, b] means I have to take b before a.
This time, I don't just say whether it's possible.
I need to return an order to take all the courses.
If it's impossible, I return an empty list."

"I have a few quick questions before I start."

"Just to confirm, does [a, b] mean b comes before a?"
→ I'll assume yes.

"If there are several valid orders, can I return any of them?"
→ I'll assume yes.

"If it's impossible, should I return an empty list?"
→ I'll assume yes.

"Can the prerequisite list be empty?"
→ I'll assume yes, and then any order of all the courses works.

"Okay, so this is the same cycle check as before.
If there's a cycle, there's no valid order.
If there isn't, I need to list every course
so each one comes after all of its prerequisites."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
numCourses = 2, prerequisites = [[1, 0]]
```
"Course 1 needs 0. Answer: [0, 1]."

```
numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
```
"0 has to come first, then 1 and 2 in either order, then 3.
Answer: [0, 1, 2, 3] or [0, 2, 1, 3]."

```
numCourses = 2, prerequisites = [[1, 0], [0, 1]]
```
"They need each other, so it's a cycle. Answer: []."

"A few edge cases:"
- "No prerequisites: any order of all the courses is fine, like [0, 1, 2]."
- "One course, no pairs: answer is [0]."
- "A course that needs itself, like [0, 0]: it's a cycle, so the answer is []."
- "A course that isn't in any pair still has to appear in the output."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I build the order one course at a time, like I'm actually signing up for classes."

"Each round, I scan through all the courses I haven't taken yet,
and look for one whose prerequisites are all already taken.
I add it to my order, and start the next round."

"If I get through a round and can't find any course to take,
then everything left is stuck in a cycle, so I return an empty list."

"This works because I only ever add a course after all of its prerequisites."

"The time is O(V * (V + E)),
where V is the number of courses and E is the number of pairs.
I do up to V rounds, and each round can scan every course and every pair."

"The space is O(V + E), for the graph and the set of taken courses."

"The problem is that every round starts over from scratch.
I keep re-checking the same courses and the same prerequisites,
even though most of them didn't change since the last round."

## 4. Optimal solution

"The bottleneck is rescanning everything every round.
So I want one pass that builds the order as it goes."

"Instead of searching for the next available course over and over,
I can run DFS and add each course to the order
only after all of its prerequisites are finished."

"That way, prerequisites always land in the list first,
and the course goes in right after."

"I'll keep the same three states as the cycle check:
not visited, visiting, and done."

"The data structures I'll use are an adjacency list, two sets, and a list.
The adjacency list maps each course to its prerequisites,
so I can find them directly.
The visiting set holds the courses on my current path,
because seeing one again means there's a cycle.
The done set holds courses that are already finished,
so I never process them twice.
The order list holds the final answer."

"As I go through each course, I run DFS on it."

"When I reach a course that's in visiting, I return False, because it's a cycle."

"When I reach a course that's in done, I return True,
because it's already in the order."

"Otherwise, I mark it as visiting and finish all its prerequisites first.
If any of them fails, I return False."

"When all of them are fine, I move the course from visiting to done,
and add it to the order."

"If any DFS finds a cycle, I return an empty list.
At the end, I return the order."

"The time is O(V + E).
Each course is processed once, because of the done set,
and each prerequisite pair is looked at once."

"The space is O(V + E).
The adjacency list stores every pair,
the sets and the order hold up to V courses,
and the call stack can go V deep."

"So I go from O(V * (V + E)) down to O(V + E)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called findOrder that takes self, numCourses, and prerequisites."

"I'll start by building the graph.
I'll create an empty list called adj,
and loop numCourses times to give each course its own empty list.
I make a list for every course, so courses with no pairs still have an entry."

"Then I loop over each pair, unpacking it into course and pre.
I append pre to adj[course].
So adj[course] holds everything that course depends on."

"Next, I'll create an empty set called visiting.
It holds the courses on my current DFS path."

"Then an empty set called done.
It holds the courses that are finished and already in the order."

"And an empty list called order.
This is the answer I'll return."

"Now I'll define a helper called dfs that takes a course.
It returns True if there's no cycle from this course,
and False if there is one."

"First thing inside it, I check if the course is in visiting.
If it is, I've come back to a course on my current path.
That's a cycle, so I return False."

"Then I check if the course is in done.
If it is, it's already in the order, so I return True right away."

"If neither is true, I add the course to visiting,
because it's now on my current path."

"Then I loop over each pre in adj[course].
For each one, I call dfs on it.
If it returns False, there's a cycle below, so I return False right away."

"If the loop finishes, every prerequisite is already in the order.
So now it's safe to add this course."

"I remove the course from visiting, because I'm leaving this path.
I add it to done, so I never process it again.
And I append it to order.
I add it here, after its prerequisites,
so it always comes after them in the list."

"Then I return True."

"Now I loop over every course from 0 to numCourses - 1.
I loop over all of them, so courses that aren't in any pair still get added."

"For each course, I call dfs.
If it returns False, there's a cycle, so I return an empty list."

"If the loop finishes, every course is in the order,
and every course comes after its prerequisites.
So I return order."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[[1, 0]]: dfs(0) has no prerequisites, so 0 is added to the order.
  dfs(1) checks 0, which is done, so 1 is added after it.
  The answer is [0, 1], which matches."
- "Shared prerequisite: dfs(0) adds 0 first.
  dfs(1) sees 0 is done, so it adds 1.
  dfs(2) does the same and adds 2.
  dfs(3) sees 1 and 2 are done, so it adds 3.
  The answer is [0, 1, 2, 3], which is one of the valid orders."
- "[[1, 0], [0, 1]]: dfs(0) adds 0 to visiting and goes to 1.
  dfs(1) goes back to 0, which is still in visiting.
  That's a cycle, so the answer is [], which matches."
- "No prerequisites: every dfs adds its course right away.
  The answer is [0, 1, 2, ...]."
- "One course: the answer is [0]."
- "[0, 0]: dfs(0) adds 0 to visiting, then its prerequisite is 0 again,
  which is in visiting. The answer is []."

"The output matches what I expected for all of them."

"To recap, time is O(V + E) and space is O(V + E)."

"If the chain of courses could be very long,
the recursion might hit Python's limit of about 1000.
In that case, I'd use Kahn's algorithm.
That's BFS with in-degree counts:
I start with every course that has no prerequisites,
add each one to the order as I take it,
and lower the count for the courses that depend on it.
If the order ends up shorter than numCourses, there's a cycle."
"""
class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = []
        for i in range(numCourses):
            adj.append([])

        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()
        done = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True

            visiting.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            done.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order