"""
Time Based Key Value Store - Explanation

Design a time-based key-value data structure that can store multiple values for the same 
key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value 
value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called 
previously, with timestamp_prev <= timestamp. If there are multiple such values, it 
returns the value associated with the largest timestamp_prev. If there are no values, 
it returns "".
Example 1:
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"



## Time Based Key-Value Store (Timemap)

**Clarify:**
- so I need a data structure that stores values for a key, but each value also comes with a timestamp
- set just adds a new value at a given timestamp for a key
- get needs to return the value for a key at or before a given timestamp, basically the most recent one that's not in the future
- if nothing qualifies, I return an empty string

**Brute force:**
- for get, I could just loop through every stored value for that key and find the latest one that's less than or equal to the timestamp
- that's O(n) per get call, which works but isn't ideal if there's a lot of history for a key

**Optimize:**
- since timestamps are always added in increasing order through set, the list for each key is already sorted by time
- that sorted property means I can binary search it instead of scanning linearly, which mitigates the O(n) cost and brings get down to O(log n)

**Key observation:**
- because set always appends, I never have to worry about inserting out of order, the list is naturally sorted
- during the binary search, I'm not looking for an exact match, I'm looking for the latest timestamp that's still less than or equal to what's asked
- so every time the stored timestamp qualifies, I save it as a possible answer and keep pushing right to see if there's something even closer, and if it doesn't qualify, I pull back left

**Approach:**
- use a dictionary where each key maps to a list of (timestamp, value) pairs
- set just appends a new pair to that list
- get does binary search on that list, tracking the best valid answer found, and finally returns it

**While coding:**
- first I define the class Timemap
- in the constructor, I set up self.time_map as an empty dictionary
- for the set method, I take key, value, and timestamp
- I check if the key is already in the dictionary, if not I initialize it with an empty list
- then I append a tuple of timestamp and value to that list
- for the get method, I take key and timestamp
- first I check if the key even exists, if not I just return an empty string right away
- I grab the list of values for that key
- I set low to 0, high to the length of that list minus 1
- I set ans to an empty string as my fallback
- I start a while loop that runs while low is less than or equal to high
- I calculate mid, then pull out the stored_time and stored_value at that mid index
- I check if stored_time is less than or equal to the timestamp I'm looking for
- if it is, that's a valid candidate, so I save stored_value into ans, and then push low up to mid plus 1, trying to find something even closer
- if it's not valid, meaning the stored time is too far in the future, I bring high down to mid minus 1
- once the loop ends, I return ans

**Edge cases:**
- if get is called on a key that was never set, I return empty string immediately
- if the timestamp asked for is earlier than every stored timestamp, nothing qualifies, so ans stays empty string
- if there's only one stored value for a key, the binary search just checks that one value directly

**Complexity:**
- set is O(1), I'm just appending to a list
- get is O(log n), where n is the number of values stored for that particular key, since I'm binary searching that list
- space is O(n) overall, since I'm storing every single value that ever gets set
"""
class Timemap:

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.time_map:
            return ""
        values = self.time_map[key]
        low = 0
        high = len(values) - 1
        ans = ""
        while low <= high:
            mid = (low + high) // 2
            stored_time = values[mid][0]
            stored_value = values[mid][1]
            if stored_time <= timestamp:
                ans = stored_value
                low = mid + 1
            else:
                high = mid - 1
        return ans



    