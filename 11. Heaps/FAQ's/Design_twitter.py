"""
Design Twitter

Create a simplified version of a social media platform similar to Twitter. Users should be able to post tweets, follow or unfollow other users, and view the 10 most recent tweets in their news feed.
Implement the Twitter class as follows:
Twitter() initializes the twitter object
void postTweet(int userId, int tweetId) It composes a new tweet with ID tweetId by the user userId. All tweetId's will be unique.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. The news feed should only show posts from users the user follows or from the user themself, with tweets arranged from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId. Input will be given such that user with followerId will not be following user with followeeID at the time of function call.
void unfollow(int followerId, int followeeId) The user with ID followerId unfollowed the user with ID followeeId. Input will be given such that user with followerId will be following user with followeeID at the time of function call.

Example 1:
Input: [postTweet(1, 2), postTweet(2, 6), getNewsFeed(1), follow(1, 2), getNewsFeed(1), unfollow(1, 2), postTweet(1,7), getNewsFeed(1)]
Output:[null, null, [2], null, [6, 2], null, [7, 2]]
Explanation:
postTweet(1, 2): User with userId 1 posts tweet with tweetId 2.
postTweet(2, 6): User with userId 2 posts tweet with tweetId 6.
getNewsFeed(1): Outputs feed of userId 1 = [2].
follow(1, 2): User with userId 1 follows user with userId 2.
getNewsFeed(1): Outputs feed of userId 1 = [6, 2], it contains the news of userId 2 as well.
unfollow(1, 2): User with userId 1 unfollows user with userId 2.
postTweet(1,7): User with userId 1 posts tweet with tweetId 7.
getNewsFeed(1): Outputs feed of userId 1 = [7, 2].

Example 2:
Input: [follow(2, 1), follow(1, 2), postTweet(1, 6), getNewsFeed(1), getNewsFeed(2), unfollow(2, 1), getNewsFeed(2)]
Output: [null, null, null, [6], [6], null, []]
Explanation:
follow(2, 1): User with userId 2 follows user with userId 1.
follow(1, 2): User with userId 1 follows user with userId 2.
postTweet(1, 6): User with userId 1 posts tweet with tweetId 6.
getNewsFeed(1): Outputs feed of userId 1 = [6].
getNewsFeed(2): Outputs feed of userId 2 = [6]. This includes tweets of userId 1 as well.
unfollow(2, 1): User with userId 2 unfollows user with userId 1.
getNewsFeed(2): Outputs feed of userId 2 = [], its empty as userId 2 no longer follows userId 1.




# Design Twitter: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I need to design a simple version of Twitter.
It has four things it needs to support."

- "postTweet: a user posts a tweet with a given id."
- "getNewsFeed: get the 10 most recent tweets,
  from the user themselves and from everyone they follow,
  ordered from newest to oldest."
- "follow: one user starts following another."
- "unfollow: one user stops following another."

"Quick things I'd confirm:
should a user always see their own tweets? I'll assume yes.
What if someone follows themselves, or unfollows someone they don't follow?
I'll assume nothing should break.
Are tweet ids unique? I'll assume yes."

"So the main question is, how do I store things
so getNewsFeed is fast?"

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll keep a global clock, so every tweet gets a time.
For every user, I'll store a list of their tweets, with the time.
And for every user, I'll store a set of people they follow."

"postTweet, follow, and unfollow are super simple.
I just add to the list or the set."

"Now for getNewsFeed, the naive way is,
I take the user and everyone they follow,
and I collect every single tweet from all of them into one big list.
Then I sort that list by time, newest first,
and return the first 10. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"postTweet is just appending to a list, so big O of 1.
follow and unfollow are just adding or removing from a set,
so big O of 1 on average."

"Now getNewsFeed.
To ease out computations, I'll say T is the total number of tweets
from the user and everyone they follow."

"First portion, collecting all the tweets, that's big O of T."

"Next portion, sorting them, that's T logarithmic of T."

"Then taking the first 10 is just big O of 1."

"So the overall time for getNewsFeed is T plus T log T,
which is near about big O of T log T."

"And here's the problem, agreed?
T keeps growing forever, because people keep posting.
So every getNewsFeed gets slower and slower,
even though I only ever need 10 tweets."

### Space complexity

"Am I using any extra space for getNewsFeed?
Yes, the big list that holds all T tweets, that's big O of T."

"Obviously the interviewer will not be happy with this,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
Each person's tweet list is already sorted by time, right?
Because I append them in the order they were posted.
So the newest tweet of each person is just the last one in their list."

"That means this is nothing but merging sorted lists.
Same idea as merge K sorted lists,
except I only need the top 10."

"So I'll use a heap.
In case you don't know about it, nothing to worry about.
Just remember, it gives me the minimum value every time.
I want the newest tweet, so the biggest time.
So I'll store the time as negative,
which makes the newest tweet the smallest, right at the top."

"What is the next step?
I take the user and everyone they follow, and put them in a set.
I always add the user themselves, so they see their own tweets."

"For each person, if they have any tweets,
I push only their newest tweet into the heap.
I store the negative time, the tweet id, the person, and the index of that tweet."

"Why do I store the person and the index?
Because when I pop a tweet,
I need to know where to go next, the person's next older tweet."

"Now I pop from the heap.
That's the newest tweet among everyone, so I add it to the feed."

"Then I check, does this person have an older tweet?
If the index is more than 0, yes.
So I move the index back by 1, and push that older tweet into the heap."

"I keep doing this till I have 10 tweets, or the heap is empty.
Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"postTweet is still appending to a list, so big O of 1."

"follow and unfollow are adding to and removing from a set,
so big O of 1 on average."

"Now getNewsFeed.
I'll say F is the number of people, the user plus everyone they follow."

"First portion, building the set of people.
I go through everyone they follow, so that's big O of F."

"Next portion, pushing each person's newest tweet.
That's at most F pushes, and the heap is at most size F,
so each push is logarithmic of F.
So this portion is F into logarithmic of F."

"Next portion, the while loop.
For how many times is it running?
At max 10 times, because I stop once the feed has 10 tweets.
Inside, I do one pop and at most one push,
and each one is logarithmic of F.
So this portion is 10 into 2 into logarithmic of F,
which is nothing but big O of log F."

"So the overall time for getNewsFeed is
F plus F log F plus log F,
which is near about big O of F log F."

"If I compare with the brute force,
that was T log T, where T is all the tweets ever posted by those people.
Now it's F log F, where F is just the number of people.
And F doesn't grow when people post more tweets,
so this is much better."

### Space complexity

"What about the space complexity?"

"For getNewsFeed, can I say it's big O of F? I can.
The set holds F people, the heap holds at most F tweets,
and the feed holds at most 10."

"For the whole class, I'm storing every tweet ever posted,
and every follow relationship.
So overall, it's big O of total tweets plus total follows.
But that's just storing the data, I can't avoid that."

## Code

"In the constructor, I set time to 0.
I'll increase it every time someone posts,
so a bigger time means a newer tweet."

"Then I make tweets, a dictionary from userId to a list of (time, tweetId).
The list goes from oldest to newest."

"And following, a dictionary from userId to a set of the people they follow.
I use a set, so following the same person twice doesn't duplicate,
and unfollowing is big O of 1."

"In postTweet, if this user has no list yet, I make an empty one.
Then I append (time, tweetId), and add 1 to time."

"In getNewsFeed, I make a set called people, and add userId.
If the user follows anyone, I add all of them to people."

"Then I make an empty list called heap."

"For every person in people,
if they have tweets, I take the last index, which is their newest tweet.
I get the time and tweetId at that index,
and push negative time, tweetId, person, and index into the heap."

"Then I make an empty list called feed."

"I loop while the heap isn't empty, and the feed has less than 10 tweets."

"Inside, I pop the top, and unpack it into negTime, tweetId, person, and index.
I append tweetId to the feed."

"Then, if index is more than 0, this person has an older tweet.
So I move index back by 1,
get that older tweet, and push it into the heap."

"Once the loop ends, I return feed."

"In follow, if the follower has no set yet, I make an empty one.
Then I add followeeId to it."

"In unfollow, if the follower has a set, I discard followeeId.
I use discard instead of remove,
because remove crashes if the person isn't in the set,
and discard just does nothing."

"And since getNewsFeed always adds the user themselves,
even if they unfollow themselves, they still see their own tweets."

## Quick check

```
postTweet(1, 5)
getNewsFeed(1)   → [5]
follow(1, 2)
postTweet(2, 6)
getNewsFeed(1)   → [6, 5]
unfollow(1, 2)
getNewsFeed(1)   → [5]
```

- "postTweet(1, 5): user 1's list is [(0, 5)], and time becomes 1."
- "getNewsFeed(1): people is {1}. I push tweet 5. I pop it. The feed is [5]. Correct."
- "follow(1, 2): user 1 now follows {2}."
- "postTweet(2, 6): user 2's list is [(1, 6)], and time becomes 2."
- "getNewsFeed(1): people is {1, 2}.
  I push (-0, 5) and (-1, 6).
  -1 is smaller, so I pop tweet 6 first, then tweet 5.
  The feed is [6, 5]. Correct."
- "unfollow(1, 2): user 1 follows nobody now."
- "getNewsFeed(1): people is {1}, so the feed is [5]. Perfect."

"If a user has no tweets and follows nobody,
nothing goes into the heap, so I return an empty list."
"""
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}          # userId -> list of (time, tweetId), oldest to newest
        self.following = {}       # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        people = set()
        people.add(userId)
        if userId in self.following:
            for followeeId in self.following[userId]:
                people.add(followeeId)

        heap = []
        for person in people:
            if person in self.tweets and len(self.tweets[person]) > 0:
                index = len(self.tweets[person]) - 1
                time, tweetId = self.tweets[person][index]
                heapq.heappush(heap, (-time, tweetId, person, index))

        feed = []
        while heap and len(feed) < 10:
            negTime, tweetId, person, index = heapq.heappop(heap)
            feed.append(tweetId)
            if index > 0:
                index = index - 1
                time, olderTweetId = self.tweets[person][index]
                heapq.heappush(heap, (-time, olderTweetId, person, index))

        return feed

    def follow(self, followerId, followeeId):
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
            


