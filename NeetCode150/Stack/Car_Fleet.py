"""
Car Fleet - Explanation

There are n cars traveling to the same destination on a one-lane 
highway. You are given two arrays of integers position and speed, 
both of length n.
    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up 
to another car and then drive at the same speed as the car ahead 
of it.A car fleet is a non-empty set of cars driving at the same 
position and same speed. A single car is also considered a car 
fleet.If a car catches up to a car fleet the moment the fleet 
reaches the destination, then the car is considered to be part of 
the fleet.Return the number of different car fleets that will 
arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) 
become a fleet, meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3




## Car Fleet

**Clarify:**
- Cars moving toward the same target, each with a position and speed
- A car catches up to a slower car ahead and they merge into one fleet, moving at the slower speed from then on
- Return the number of distinct fleets that arrive at the target

**Brute force:**
- Simulate every car's movement over time, checking collisions/merges as they happen
- Complicated and slow — hard to reason about time steps

**Optimize:**
- Sort cars by position, closest to target first
- Use a stack of arrival TIMES — process cars in order from closest to farthest
- O(n log n) from the sort, O(n) for the single pass

**Key observation:**
- A car closer to the target that's SLOWER still acts as a "wall" — any car behind it that would arrive LATER (even if physically faster) gets stuck behind it and merges into the same fleet
- Sorting by position (closest to target first) means you always process the "wall" cars before the cars that might catch up to them
- If a car's arrival time is <= the time of the fleet directly ahead, it catches up and merges — no new fleet forms
- If a car's arrival time is greater, it never catches the fleet ahead, so it forms its own new fleet

**Approach:**
- Pair each car's (position, speed), sort by position descending (closest to target first)
- For each car, compute time = (target - position) / speed
- stack holds the arrival times of confirmed distinct fleets, in order processed
- if stack is empty OR time > stack[-1]: this car cannot catch the fleet ahead → push its time as a new fleet
- if time <= stack[-1]: it merges into the fleet ahead → do nothing
- Return len(stack) — the number of distinct fleets

**While coding:**
- Sort with reverse=True on (position, speed) pairs — sorts by position descending since position is the first tuple element
- Only compare against stack[-1] (the most recently confirmed fleet), not the whole stack — because if this car doesn't catch the closest fleet ahead, it definitely can't catch any fleet beyond that
- No popping happens here (unlike Daily Temperatures) — once a fleet is confirmed, it stays; you're only ever deciding "new fleet or merge," never re-evaluating an old one

**Edge cases:**
- Single car → always forms its own fleet, stack ends with 1 entry
- All cars end up merging into one fleet → stack only ever has 1 entry the whole time
- Cars already sorted / all same speed → still works, sort handles any input order

**Complexity:**
- Time: O(n log n) — dominated by the sort; the single pass after is O(n)
- Space: O(n) — worst case, every car forms its own fleet, stack holds n entries
"""
class Solution:
    def carFleet(self, target, position, speed):

        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort closest to target -> farthest
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:

            # Time this car would take to reach target
            time = (target - pos) / spd

            # If stack is empty, this starts a new fleet
            if not stack:
                stack.append(time)

            # Takes longer than fleet ahead -> cannot catch it
            # So this becomes a new fleet
            elif time > stack[-1]:
                stack.append(time)

            # If time <= stack[-1]:
            # it catches the fleet ahead, so do nothing

        return len(stack)


# Example
target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

obj = Solution()
print(obj.carFleet(target, position, speed))

"""
CAR FLEET — SHORT EXPLANATION

Goal:
Find how many separate groups of cars reach the target.

1. Pair each car's (position, speed).

2. Sort cars by position:
   closest to target → farthest.

3. Calculate each car's arrival time:

   time = (target - position) / speed

4. Keep fleet arrival times in a stack.

5. Compare each car with the fleet directly ahead:

   current_time <= stack top
   → catches the fleet ahead
   → SAME fleet
   → don't push

   current_time > stack top
   → cannot catch the fleet ahead
   → NEW fleet
   → push time

6. Number of fleets = len(stack)


Example idea:

stack = [3]

new time = 2
2 <= 3 → catches fleet → don't push

new time = 5
5 > 3 → new fleet → push

stack = [3, 5]

Answer = 2 fleets


Complexity:
Time: O(n log n) → sorting dominates
Space: O(n) → stack/pairs
"""