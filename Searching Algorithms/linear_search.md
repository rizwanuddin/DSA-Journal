# Linear Search

## What is it?

Go through every element one by one from left to right until you find what you're looking for (or reach the end).

That's it. No sorting needed, no special structure. Just loop and check.

---

## How it works

```
Array: [4, 2, 9, 7, 5]
Target: 7

Step 1 → check 4. Not 7.
Step 2 → check 2. Not 7.
Step 3 → check 9. Not 7.
Step 4 → check 7. ✅ Found at index 3.
```

---

## Java Code

```java
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i; // return index where found
        }
    }
    return -1; // not found
}
```

---

## Time & Space Complexity

| Case | Time | Why |
|------|------|-----|
| Best case | O(1) | Target is the first element |
| Average case | O(n) | Target is somewhere in the middle |
| Worst case | O(n) | Target is last OR not in array at all |
| Space | O(1) | No extra memory used |

> The worst case is when the element is not present — you still check every single element before giving up.

---

## When to use it

- Array is **unsorted** (binary search won't work here)
- Array is **very small** (not worth sorting just to search)
- You're searching a **linked list** (no random access, so no binary search)
- You need to find **all occurrences**, not just one

---

## When NOT to use it

- Array is large **and** sorted → use Binary Search (O(log n)) instead
- You're doing many repeated searches → sort once, then binary search every time

---

## Common Interview Variations

### 1. Find first occurrence
Standard linear search — return the index as soon as you find it.

### 2. Find last occurrence
```java
int lastIndex = -1;
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
        lastIndex = i; // keep updating, don't return early
    }
}
return lastIndex;
```

### 3. Find all occurrences
```java
List<Integer> result = new ArrayList<>();
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
        result.add(i);
    }
}
return result;
```

### 4. Search in a 2D array
```java
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] == target) return true;
    }
}
return false;
```

### 5. Find minimum / maximum element
```java
int min = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
}
```
> This is linear search logic — scanning every element to find the answer.

---

## Key Things Interviewers Check

- Do you handle **empty array** edge case?
- Do you return `-1` (not `0`) when not found?
- Do you know the difference between returning **index** vs returning **value**?
- Can you adapt it for 2D arrays, strings, linked lists?
- Do you know when to use linear vs binary search?

---

## Quick Comparison: Linear vs Binary Search

| | Linear Search | Binary Search |
|---|---|---|
| Array needs to be sorted? | ❌ No | ✅ Yes |
| Time complexity | O(n) | O(log n) |
| Works on linked list? | ✅ Yes | ❌ No |
| Simple to implement? | ✅ Yes | Slightly harder |

---

## One-liner to Remember

> Linear search = check every element left to right. O(n) worst case. Use when unsorted or small.