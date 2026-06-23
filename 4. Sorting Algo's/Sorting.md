# Sorting Algorithms — Bubble, Insertion & Selection

Interview answers, when to use each, complexity tables, and full code in Java and Python.

---

## 1. How They Work — Interview Style

### 🫧 Bubble Sort

> "Bubble sort works by repeatedly scanning through the array and comparing each pair of neighboring elements. If they're out of order, we swap them. After each full pass, the largest unsorted element has *bubbled* to its correct position on the right — like a heavy bubble rising in water. We keep doing passes, shrinking the window by one each time. The key optimization is the early-exit flag — if a full pass has zero swaps, the array is already sorted and we stop early. That's what gives us O(n) best case."

**Memory hook:** Neighbors fight. Heavy ones rise. 🫧

---

### 🃏 Insertion Sort

> "Insertion sort is like sorting playing cards in your hand. The left side of the array is always sorted. For each new element, I save it as the `key`, then shift every sorted element that's larger than it one step to the right — creating a gap — and drop the key into that gap. It's naturally adaptive: if the array is already sorted, the inner loop never runs, giving O(n) best case."

**Memory hook:** Pick a card, slide it left to fit. 🃏

---

### 🏆 Selection Sort

> "Selection sort divides the array into a sorted left side and unsorted right side. Each pass scans the *entire* unsorted portion to find the minimum element, then swaps it into the first unsorted position. There's no early exit — it always does O(n²) comparisons regardless of input. But it does exactly one swap per pass, which makes it useful when write operations are expensive."

**Memory hook:** Scan everything, grab the minimum, place it on the shelf. 🏆

---

## 2. Complexity

### Time Complexity

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) ✅ | O(n²) | O(n²) |
| Insertion Sort | O(n) ✅ | O(n²) | O(n²) |
| Selection Sort | O(n²) ❌ | O(n²) | O(n²) |

> Bubble and Insertion get O(n) best case because they can detect a sorted array early. Selection never can — it always scans everything.

### Properties

| Property | Bubble | Insertion | Selection |
|----------|--------|-----------|-----------|
| Space | O(1) | O(1) | O(1) |
| Stable? | ✅ Yes | ✅ Yes | ❌ No |
| Adaptive? | ✅ Yes (with flag) | ✅ Yes (naturally) | ❌ No |
| In-place? | ✅ Yes | ✅ Yes | ✅ Yes |
| Swaps per pass | Many (adjacent) | 1 insert | Exactly 1 |
| Best for | Teaching | Nearly sorted | Min writes |

**Stable** means equal elements keep their original relative order. Selection is not stable because long-range swaps can move equal elements past each other.

**Adaptive** means the algorithm runs faster on already/nearly sorted input. Selection is never adaptive — it always does the same amount of work.

---

## 3. When to Use Which

| Scenario | Bubble | Insertion | Selection |
|----------|--------|-----------|-----------|
| Already sorted | ✅ O(n) | ✅ O(n) best | ❌ O(n²) always |
| Nearly sorted | ⚠️ OK with flag | ✅ Best choice | ❌ Still O(n²) |
| Reverse sorted | ❌ Worst case | ❌ Worst case | ❌ Worst case |
| Small array (<20) | ⚠️ Works | ✅ Preferred | ⚠️ Works |
| Min memory writes | ❌ Many swaps | ⚠️ Moderate | ✅ Exactly 1/pass |
| Need stable sort | ✅ Stable | ✅ Stable | ❌ Not stable |
| Teaching / demo | ✅ Most visual | ✅ Intuitive | ✅ Simple logic |

### Plain-language rules

- **Use Insertion Sort** when the array is small (< ~20 elements) or nearly sorted. Best of the three in practice. Python's built-in `sort()` (Timsort) uses it internally for small runs.
- **Use Bubble Sort** mainly for teaching and demos. Always mention the early-exit flag when writing it — without it, best case is still O(n²).
- **Use Selection Sort** only when minimizing write operations matters — e.g., writing to flash memory where writes are slow and expensive. It does exactly n−1 swaps total across the whole sort.
- **Use none of these** for large unsorted data. Switch to Merge Sort O(n log n) or Quick Sort O(n log n) average. All three of these are O(n²) and will time out on large inputs.

---

## 4. Common Interview Questions

**"What's the difference between bubble and selection sort?"**

Both place one element per pass — but *how* is different. Bubble does it accidentally through many adjacent swaps. Selection does it deliberately by scanning the entire remaining array once and doing a single swap. Selection always does exactly one swap per pass; bubble can do many.

**"Why is selection sort not stable?"**

Because it does long-range swaps. Example: `[3a, 3b, 1]`. To place `1` first, we swap it with `3a`, giving `[1, 3b, 3a]`. Now `3a` and `3b` are out of original order — that's instability.

**"When is insertion sort O(n)?"**

When the array is already sorted. The inner `while` condition fails immediately on every pass, so it never executes. The outer loop still runs n−1 times, but each pass does only one comparison and zero writes.

**"Which has the fewest memory writes?"**

Selection sort. It does exactly n−1 swaps total across the whole sort — one per pass. Insertion does fewer writes than bubble per insertion, but can still do O(n) writes per pass. Bubble is worst — up to 2 writes per comparison.

**"Should you use `break` to exit loops early?"**

Functionally fine, but in CS 146 the preferred approach is putting the exit condition in the loop header — e.g. `for (int i = 0; i < n-1 && !sorted; i++)`. This keeps the termination condition in one place, which makes it easier to write and prove a loop invariant. With `break`, the loop has two exit points, which complicates formal reasoning.

---

## 5. Code

### Bubble Sort — Java

```java
public static void bubbleSort(int[] arr) {
    int n = arr.length;
    boolean sorted;

    for (int i = 0; i < n - 1 && !sorted; i++) {
        sorted = true;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                sorted = false;
            }
        }
    }
}
```

### Bubble Sort — Python

```python
def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        sorted_flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False
        if not sorted_flag:
            break
        i += 1
```

---

### Insertion Sort — Java (shift-based)

```java
public static void insertionSort(int[] arr) {
    int n = arr.length;

    for (int i = 1; i < n; i++) {
        int key = arr[i];        // save element to insert
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]; // shift right
            j--;
        }

        arr[j + 1] = key;        // drop key into gap
    }
}
```

### Insertion Sort — Python (shift-based)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]         # save element to insert
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift right
            j -= 1

        arr[j + 1] = key     # drop key into gap
```

> There's also a swap-based version (walk `j` backwards, swap adjacent pairs until in place). It produces the same result and has the same complexity but does 2 writes per step instead of 1. Both are valid — shift-based is more efficient.

---

### Selection Sort — Java

```java
public static void selectionSort(int[] arr) {
    int n = arr.length;

    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }

        // swap min into position
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
```

### Selection Sort — Python

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

## 6. One-Line Summary

| Algorithm | One line |
|-----------|----------|
| Bubble | Neighbors fight, heavy ones rise. Use for teaching — always add early-exit flag. |
| Insertion | Pick next element, shift sorted side right, drop it in. Best for small/nearly-sorted arrays. |
| Selection | Scan all remaining, find min, swap once. Never adaptive. Use when writes are expensive. |
| None of these | For large data, use Merge Sort or Quick Sort — O(n log n). |