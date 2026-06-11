# Binary Search

## What is it?

Instead of checking every element, you cut the search space in **half** each time.

Works only on a **sorted array**. Every step you pick the middle element and decide — is the target to the left or to the right? Keep halving until you find it or run out of space.

---

## How it works

```
Array: [2, 4, 7, 9, 13, 18, 25]
Target: 9

low=0, high=6 → mid=3 → arr[3]=9 ✅ Found at index 3.

Another example — Target: 18

low=0, high=6 → mid=3 → arr[3]=9.  9 < 18, so go RIGHT → low=4
low=4, high=6 → mid=5 → arr[5]=18. ✅ Found at index 5.

Another example — Target: 3

low=0, high=6 → mid=3 → arr[3]=9.  9 > 3,  so go LEFT  → high=2
low=0, high=2 → mid=1 → arr[1]=4.  4 > 3,  so go LEFT  → high=0
low=0, high=0 → mid=0 → arr[0]=2.  2 < 3,  so go RIGHT → low=1
low > high → ❌ Not found. Return -1.
```

---

## Java Code — Iterative (preferred in interviews)

```java
public static int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2; // safer than (low+high)/2 — avoids overflow

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;  // target is in RIGHT half
        } else {
            high = mid - 1; // target is in LEFT half
        }
    }
    return -1; // not found
}
```

## Java Code — Recursive

```java
public static int binarySearch(int[] arr, int low, int high, int target) {
    if (low > high) return -1; // base case: not found

    int mid = low + (high - low) / 2;

    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) return binarySearch(arr, mid + 1, high, target);
    else return binarySearch(arr, low, mid - 1, target);
}
```

---

## Time & Space Complexity

| Case | Time | Why |
|------|------|-----|
| Best case | O(1) | Target is exactly the middle element |
| Average case | O(log n) | Halving the array each time |
| Worst case | O(log n) | Target is at the edge or not present |
| Space (iterative) | O(1) | No extra memory |
| Space (recursive) | O(log n) | Call stack builds up log n deep |

> log₂(1000) ≈ 10. So even in an array of 1000 elements, worst case is just 10 comparisons.

---

## The mid formula — why not (low + high) / 2?

```java
// ❌ Can overflow if low and high are both large ints
if numbers are huge:

low = 2,000,000,000
high = 2,100,000,000

Then:

low + high = 4,100,000,000

That is bigger than Java/Python int can safely store.
int mid = (low + high) / 2;

// ✅ Safe — subtracts first, so sum never exceeds Integer.MAX_VALUE
int mid = low + (high - low) / 2;
```
Interviewers notice this. Always use the safe version.

---

## When to use it

- Array is **sorted**
- You need O(log n) search instead of O(n)
- Searching in a range of numbers (search space problems)
- Finding a boundary — first/last occurrence, insert position

---

## When NOT to use it

- Array is **unsorted** → sort first (O(n log n)) or just use linear search
- Data is in a **linked list** → no random index access, binary search won't work

---

## Common Interview Variations

### 1. Find first occurrence of target (duplicates exist)
```java
int result = -1;
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) {
        result = mid;   // save it, but keep going LEFT
        high = mid - 1;
    } else if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
}
return result;
```

### 2. Find last occurrence of target
```java
int result = -1;
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) {
        result = mid;   // save it, but keep going RIGHT
        low = mid + 1;
    } else if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
}
return result;
```

### 3. Count occurrences of target
```java
// firstOccurrence and lastOccurrence using above two methods
int count = lastOccurrence - firstOccurrence + 1;
```

### 4. Find insert position (LeetCode #35)
> Where would target go if inserted to keep array sorted?
```java
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
}
return low; // low is the insert position when not found
```

### 5. Search in rotated sorted array (LeetCode #33)
> Array like [4, 5, 6, 7, 0, 1, 2] — sorted but rotated at some pivot.
```java
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;

    if (arr[low] <= arr[mid]) { // LEFT half is sorted
        if (target >= arr[low] && target < arr[mid]) high = mid - 1;
        else low = mid + 1;
    } else { // RIGHT half is sorted
        if (target > arr[mid] && target <= arr[high]) low = mid + 1;
        else high = mid - 1;
    }
}
return -1;
```

### 6. Find peak element (LeetCode #162)
> Peak = element greater than its neighbors.
```java
while (low < high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] > arr[mid + 1]) high = mid;
    else low = mid + 1;
}
return low; // low == high == peak index
```

### 7. Square root (integer part) without sqrt()
```java
long low = 0, high = x;
while (low <= high) {
    long mid = low + (high - low) / 2;
    if (mid * mid == x) return (int) mid;
    else if (mid * mid < x) low = mid + 1;
    else high = mid - 1;
}
return (int) high; // floor of sqrt
```

---

## Key Things Interviewers Check

- Do you use `low + (high - low) / 2` instead of `(low + high) / 2`?
- Is your `while` condition `low <= high` (not `<`)?
- Do you do `mid + 1` and `mid - 1` (not just `mid`)? Without ±1 you'll infinite loop.
- Can you adapt standard binary search for first/last occurrence?
- Do you know binary search applies to **any monotonic search space**, not just arrays?

---

## The ±1 rule — most common bug

```java
// After comparing, always move mid by 1
low = mid + 1;  // ✅ skip mid, search right
high = mid - 1; // ✅ skip mid, search left

// If you forget the ±1:
low = mid;  // ❌ infinite loop when low == mid
high = mid; // ❌ infinite loop when high == mid
```

---

## Quick Comparison: Linear vs Binary Search

| | Linear Search | Binary Search |
|---|---|---|
| Array needs to be sorted? | ❌ No | ✅ Yes |
| Time complexity | O(n) | O(log n) |
| Works on linked list? | ✅ Yes | ❌ No |
| Best for large sorted data? | ❌ No | ✅ Yes |

---

## One-liner to Remember

> Binary search = sorted array only, cut in half each step, O(log n). Always use `low + (high - low) / 2` and move `mid ± 1`.