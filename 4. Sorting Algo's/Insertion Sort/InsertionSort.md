# Insertion Sort

A reference covering two valid implementations — swap-based and shift-based — in Java and Python.

---

## Concept

Build the sorted portion one element at a time. Pick the next unsorted element and insert it into its correct position among the already-sorted left side — like sorting playing cards in your hand.

**Loop invariant:** Before iteration `i`, `arr[0..i-1]` is sorted. After iteration `i`, `arr[0..i]` is sorted.

---

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

> Best case is O(n) because the inner loop never runs if each element is already in place.

Both methods below have identical time and space complexity. The difference is only in constant-factor writes per step — not Big-O.

---

## Method 1 — Swap-based

### How it works
Walk `j` backwards. At each step, if the current element is smaller than its left neighbor, swap them. Keep swapping until it's in the right place.

**Intuition:** The element "bubbles" left one position at a time until it finds its spot.

**Writes per insertion:** 2 writes per shift (both cells update on every swap).

### Java

```java
public static void insertionSort(int[] arr) {
    int n = arr.length;

    for (int i = 1; i < n; i++) {
        int j = i;

        while (j > 0 && arr[j] < arr[j - 1]) {
            // swap arr[j] and arr[j-1]
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
            j--;
        }
    }
}
```

### Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # tuple swap
            j -= 1
```

---

## Method 2 — Shift-based (textbook)

### How it works
Save the current element as `key`. Shift all elements greater than `key` one position to the right, creating a gap. Drop `key` into the gap at the end.

**Intuition:** Slide books on a shelf to make a gap, then place your book in the gap.

**Writes per insertion:** 1 write per shift + 1 final write to place the key.

### Java

```java
public static void insertionSort(int[] arr) {
    int n = arr.length;

    for (int i = 1; i < n; i++) {
        int key = arr[i];   // save element to be inserted
        int j = i - 1;

        // shift elements greater than key one position right
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;   // place key in correct spot
    }
}
```

### Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]     # save element to be inserted
        j = i - 1

        # shift elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # place key in correct spot
```

---

## Side-by-side comparison

| Property | Swap-based | Shift-based |
|----------|------------|-------------|
| Writes per step | 2 (both cells) | 1 (right cell only) |
| Extra variable | none | `key` to hold saved value |
| `j` starts at | `i` | `i - 1` |
| Inner condition | `arr[j] < arr[j-1]` | `arr[j] > key` |
| Time complexity | O(n²) | O(n²) |
| Space complexity | O(1) | O(1) |
| Easier to derive | ✅ Yes | Needs the key idea |
| More efficient | ❌ | ✅ Fewer writes |

### Trace on [1, 3, 5, 4] — inserting 4

```
Swap-based:             Shift-based:
[1, 3, 5, 4]            key = 4
  swap 5↔4 → 2 writes   shift 5 right → 1 write
[1, 3, 4, 5]            place key → 1 write
  3 < 4, stop           [1, 3, 4, 5]

Total: 2 writes          Total: 2 writes  (same here)
```

> With a larger gap to fill (e.g. inserting 1 into [2, 3, 4, 5, 1]), swap needs 2 writes × 4 steps = 8 writes. Shift needs 1 write × 4 steps + 1 final = 5 writes.

---

## Which to use

- **Swap-based** — easier to come up with on your own, natural to reason about, fully correct. Fine for exams and interviews.
- **Shift-based** — preferred in production and textbooks. Fewer memory writes, slightly faster in practice on large inputs. Also the basis for optimized variants like binary insertion sort.

If an interviewer asks "can you optimize it?" — that's the cue to switch from swap to shift.

---

## When to use insertion sort at all

- Small arrays (< ~20 elements)
- Nearly-sorted data (best case O(n))
- As the base case inside hybrid sorts — Python's built-in `sort()` (Timsort) uses insertion sort internally for small runs
- When you need a **stable**, **in-place** sort with low overhead
Insertion Sort (Swap Version)

Initial Array:
[7, 3, 5, 1]

--------------------------------------------------

i = 1
j = 1

Compare arr[0] and arr[1]
7 > 3 ? Yes

Swap(7, 3)

[3, 7, 5, 1]

j = 0
Stop

--------------------------------------------------

i = 2
j = 2

Compare arr[1] and arr[2]
7 > 5 ? Yes

Swap(7, 5)

[3, 5, 7, 1]

j = 1

Compare arr[0] and arr[1]
3 > 5 ? No

Stop

--------------------------------------------------

i = 3
j = 3

Compare arr[2] and arr[3]
7 > 1 ? Yes

Swap(7, 1)

[3, 5, 1, 7]

j = 2

Compare arr[1] and arr[2]
5 > 1 ? Yes

Swap(5, 1)

[3, 1, 5, 7]

j = 1

Compare arr[0] and arr[1]
3 > 1 ? Yes

Swap(3, 1)

[1, 3, 5, 7]

j = 0
Stop

--------------------------------------------------

Final Sorted Array:
[1, 3, 5, 7]