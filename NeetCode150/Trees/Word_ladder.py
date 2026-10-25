"""
Word Ladder - Hard

You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.
Your goal is to transform beginWord into endWord by following the rules:
You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
Output: 4
Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

Example 2:
Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]
Output: 0
Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList





# Word Ladder: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a beginWord, an endWord, and a list of words.
I can change one letter at a time,
and every word I make along the way has to be in the list.
I need to return the number of words in the shortest sequence
from beginWord to endWord, counting both ends.
If there's no way to get there, I return 0."

"I have a few quick questions before I start."

"Do all the words have the same length?"
→ I'll assume yes.

"Are they all lowercase English letters?"
→ I'll assume yes.

"Does beginWord have to be in the list?"
→ I'll assume no. It's just the starting point.

"Does endWord have to be in the list?"
→ I'll assume yes. If it isn't, I can never land on it, so the answer is 0.

"Am I counting words, not steps?"
→ I'll assume words, so hit → hot is a length of 2.

"Okay, so I can think of every word as a node,
with an edge between two words if they differ by exactly one letter.
Then I'm looking for the shortest path from beginWord to endWord."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
beginWord = "hit", endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
```
"hit → hot → dot → dog → cog. That's 5 words. Answer: 5."

```
beginWord = "hit", endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
```
"cog isn't in the list, so I can never reach it. Answer: 0."

"A few edge cases:"
- "endWord is one letter away from beginWord, like hit → hot
  with hot in the list. Answer: 2."
- "The list has endWord, but no path connects to it. Answer: 0."
- "beginWord also shows up in the list. It shouldn't cause a loop."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I build the whole graph first.
I compare every pair of words letter by letter,
and connect them if they differ by exactly one letter.
Then I run BFS from beginWord to find the shortest path to endWord."

"This works because BFS on an unweighted graph
always finds the shortest path."

"The time is O(N^2 * L),
where N is the number of words and L is the length of each word.
There are about N^2 pairs, and comparing two words takes L steps."

"The space is O(N^2), because in the worst case,
every word is connected to every other word."

"The problem is that comparing every pair is slow when the list is big.
Most pairs aren't even neighbors,
so I'm doing a lot of checks that go nowhere."

## 4. Optimal solution

"The bottleneck is comparing every word with every other word."

"Instead of comparing all pairs,
I can build each word's neighbors on the spot.
For each position in the word, I try all 26 letters.
That gives me every possible word one letter away.
Then I just check if it's in the list."

"Each word has only 26 times L possible neighbors,
so that's a lot fewer checks than comparing against all N words
when the list is big."

"The data structures I'll use are a set and a queue."

"The set holds the words I'm still allowed to use,
because checking if a word is in a set is O(1) on average."

"The queue drives the BFS,
because BFS goes level by level,
so the first time I reach endWord is the shortest path."

"As I go through the queue, I take out a word and its count.
I try changing every letter to every letter from a to z."

"When the new word is endWord, I return count + 1."

"When the new word is in the set, I remove it from the set,
and add it to the queue with count + 1.
Removing it right away works as my visited check,
so no other path can add it again."

"If the queue runs out, there's no path, so I return 0."

"The time is O(N * L^2 * 26), which is O(N * L^2). 
Each word goes into the queue at most once.
For each one, I try 26 letters in L positions,
and building each new word takes L steps."

"The space is O(N * L), for the set and the queue."

"So I go from O(N^2 * L) to O(N * L^2),
which is much faster when there are a lot of words
compared to how long each word is."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import deque from collections.
I'm using it as my queue, because removing from the front is O(1)."

"Then I'll make a class called Solution,
and a function called WordLadder that takes self, beginWord, endWord, and wordList."

"I'll turn wordList into a set called word_set.
That way, checking if a word is allowed is O(1) instead of scanning a list."

"Then I check if endWord is not in word_set.
If it isn't, I can never reach it, so I return 0 right away."

"Next, I'll create the queue with one item: the tuple (beginWord, 1).
The 1 means the sequence has one word so far, which is beginWord itself.
I store the word and its count together,
so each word remembers how far it is from the start."

"Now I start a while loop that runs as long as the queue isn't empty."

"Inside it, I take a word and its count from the front, using popleft."

"Then I loop i over every position in the word."

"For each position, I loop ch over every letter from a to z."

"I build new_word by taking the part before i,
putting ch in position i,
and adding the part after i.
So new_word is the same as word, with just one letter changed."

"Then I check if new_word equals endWord.
If it does, I return count + 1,
since endWord is one more word in the sequence.
Because BFS goes level by level, this is the shortest path."

"Next, I check if new_word is in word_set.
If it is, it's a valid word I haven't used yet."

"I remove it from word_set right away.
That marks it as visited,
so no other word can add it to the queue again."

"Then I add (new_word, count + 1) to the queue."

"If the while loop ends, I've tried everything I can reach,
and I never found endWord, so I return 0."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: the queue starts with (hit, 1).
  From hit, I find hot, and add (hot, 2).
  From hot, I find dot and lot, and add both with 3.
  From dot, I find dog, and add (dog, 4).
  From lot, I find log, and add (log, 4).
  From dog, changing d to c gives cog, which is endWord,
  so I return 4 + 1 = 5. That matches."
- "cog not in the list: the first check returns 0 right away.
  That matches."
- "hit to hot with hot in the list: from hit, hot is endWord,
  so I return 1 + 1 = 2."
- "endWord in the list but unreachable: the queue empties
  without hitting it, so I return 0."
- "beginWord in the list: if I make it again, it's still in the set
  the first time, so it gets added once and then removed.
  It can't loop, because once it's removed, it's never added again."

"The output matches what I expected for all of them."

"To recap, time is O(N * L^2) and space is O(N * L)."

"If I wanted to make it faster in practice,
I could run BFS from both ends at the same time.
That's called bidirectional BFS.
It has the same big-O,
but it usually explores far fewer words,
because the two searches meet in the middle."""


from collections import deque
class Solution:
    def WordLadder(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, count = queue.popleft()

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word == endWord:
                        return count + 1

                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, count + 1))

        return 0