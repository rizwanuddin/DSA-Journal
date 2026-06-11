-- In hashing the value from the original array becomes the index in the hash array.


-- A normal array stores the original elements, while a hash array is used as a frequency table. In a normal array, the index represents the position of the element. In a hash array, the index represents the value itself, and the value at that index represents how many times it appeared. This works well when the range of numbers is small and non-negative. For large values like 10^9, using an array would waste memory, so I would use a HashMap instead.

-- We use array hashing when the value range is small because it is faster and simpler. It uses direct index access, so fetching frequency is O(1). But its space complexity is O(maxValue + 1), so if the maximum value is very large, it wastes too much memory.

In that case, we use a HashMap because it stores only the elements that actually appear. HashMap is more flexible, but it has extra overhead due to hashing, buckets, and collision handling.
-- TIME COMPLEXITY : For hashing-based frequency counting, first I precompute the frequencies by iterating through the array once. That takes O(n) time. Then for each query, I directly access the frequency using either an array index or a HashMap lookup. Array access is O(1), and HashMap lookup is O(1) on average. So if there are q queries, answering all queries takes O(q). Therefore the total average time complexity is O(n + q). The space complexity is O(maxValue + 1) for array hashing and O(k) for HashMap, where k is the number of unique elements.

# Hashing Memory Limit Notes

## What is array hashing?

Array hashing means using an array to count the frequency of numbers.

Example:

```cpp
int arr[] = {1, 2, 3, 1, 2};
int hash[4] = {0};

for (int i = 0; i < 5; i++) {
    hash[arr[i]]++;
}
```

Now:

```text
hash[1] = 2
hash[2] = 2
hash[3] = 1
```

So, `hash[number]` tells us how many times that number appeared.

---

## Why array hashing is fast

Array hashing is very fast because accessing an array index takes constant time.

```cpp
hash[number]
```

Time complexity:

```text
O(1)
```

So after precomputing frequencies, fetching the count of any number is very fast.

---

## The problem with large numbers

Array hashing only works well when the number range is small.

For example, if the largest number is `12`, we can create:

```cpp
int hash[13];
```

That is fine.

But if the largest number is `10^9`, then we would need:

```cpp
int hash[1000000001];
```

This is not good because it needs too much memory.

An `int` usually takes 4 bytes.

So:

```text
10^9 integers * 4 bytes = around 4 GB
```

That is too much memory for most coding platforms.

---

## C++ memory rule for arrays

This rule is mainly for C++.

In C++, local arrays are created inside a function like `main`.

Example:

```cpp
int main() {
    int hash[1000000];
}
```

Usually, inside `main`, we can safely create arrays around:

```text
10^6
```

because local arrays use stack memory, and stack memory is limited.

---

Global arrays are created outside all functions.

Example:

```cpp
int hash[10000000];

int main() {
    // use hash here
}
```

Globally, we can usually create larger arrays, around:

```text
10^7
```

because global arrays are stored in a different memory area, not the stack.

---

## Simple rule

```text
Inside main/function: around 10^6 is usually safe
Globally: around 10^7 is usually safe
10^9 size array: not safe
```

This is a rough C++ rule for competitive programming.

---

## Important note for Java

This local/global rule is mostly for C++.

In Java, arrays are created on the heap, even if they are written inside `main`.

So in Java, the limit depends more on heap memory, not whether the array is local or global.

But the main idea is still the same:

```text
Do not create a huge array for values like 10^9.
```

---

## What should we use for large numbers?

For large numbers, we should use a map.

In C++:

```cpp
unordered_map<int, int> mp;
```

In Java:

```java
HashMap<Integer, Integer> mp = new HashMap<>();
```

A map stores only the numbers that actually appear.

Example:

```text
arr = [1000000000, 5, 1000000000]
```

A map stores:

```text
1000000000 -> 2
5 -> 1
```

It does not create an array of size `1000000001`.

---

## Interview-style explanation

Array hashing is useful when the range of numbers is small because we can use the number itself as the index and get `O(1)` access. But if the numbers are very large, like `10^9`, creating an array of size `10^9 + 1` would waste too much memory. In C++, a local array inside `main` is usually safe up to around `10^6`, while a global array can usually go up to around `10^7`. This is because local arrays use stack memory, while global arrays are stored separately. For very large values, I would use `unordered_map` in C++ or `HashMap` in Java because they store only the keys that actually appear.

---

## When to use what

```text
Small range numbers     -> Array hashing
Very large numbers      -> unordered_map / HashMap
Need sorted keys in C++  -> map
Need faster average case -> unordered_map
```

---

## Time complexity

For array hashing:

```text
Precompute: O(n) 
Fetch: O(1)
Space: O(maxValue + 1)
```

For unordered_map / HashMap:

```text
Precompute: O(n) average
Fetch: O(1) average
Space: O(number of unique elements)
```
# Array Hashing vs HashMap Mental Model

## Clean Mental Model

### Array Hashing

In array hashing, the **number itself becomes the index**.

Example:

```java
hash[5]++;
```

This means:

```text
The number 5 appeared one more time.
```

So:

```text
hash[5] = frequency of number 5
```

Array hashing does **not** have buckets, chaining, or collision handling in the normal version.

Why?

Because each number directly maps to its own index.

```text
number 1 -> hash[1]
number 2 -> hash[2]
number 3 -> hash[3]
```

So different numbers do not fight for the same place.

Array hashing is very fast because it uses direct array access.

Time to fetch:

```text
O(1)
```

But array hashing only works well when the range is small.

Example:

```java
int[] hash = new int[100001];
```

This is fine if numbers are between `0` and `100000`.

But this is not good:

```java
int[] hash = new int[1000000001];
```

This wastes too much memory if numbers go up to `10^9`.

---

### HashMap

In a HashMap, the number is **not directly used as the index**.

Instead, the number is converted internally into a bucket index.

The idea is:

```text
number -> hash function -> bucket index
```

Example idea:

```text
18 -> hash function -> bucket 2
28 -> hash function -> bucket 2
```

If two different numbers land in the same bucket, that is called a collision.

```text
bucket 2 -> 18 -> 28
```

HashMap handles these collisions internally.

HashMap is more flexible than array hashing because it can handle:

```text
large numbers
negative numbers
unknown ranges
sparse values
```

Example:

```java
HashMap<Integer, Integer> mp = new HashMap<>();

mp.put(num, mp.getOrDefault(num, 0) + 1);
```

This stores:

```text
number -> frequency
```

HashMap average fetch time:

```text
O(1)
```

But in the worst case, due to many collisions, it can become slower.

---

## Interview-Style Explanation

In array hashing, I use the value directly as the array index. For example, to count the number `5`, I increment `hash[5]`. This is direct array access, so it takes `O(1)` time.

Normal array hashing does not involve buckets or collision handling because each value has its own index. Collisions only come into play in hash tables or HashMaps, where keys are converted into bucket indexes using a hash function, and different keys may land in the same bucket.

Array hashing is faster and simpler when the range is small, but HashMap is better when the numbers are large, negative, or the range is unknown.


---

## Final takeaway

Array hashing is fast but only good when the range is small.

If the value is too large, like `10^9`, we should not create a huge array.

Use a map instead.
