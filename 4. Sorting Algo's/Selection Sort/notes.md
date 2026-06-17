# Selection Sort

## The idea in one line

> Scan the unsorted part, find the minimum, swap it to the front. Repeat.

---

## How it thinks

Imagine you have a row of numbers. You split them mentally into two sections:

```
[ sorted | unsorted ]
```

Each pass you:
1. Look through the entire unsorted section
2. Find the smallest number
3. Swap it to the front of the unsorted section
4. That position is now sorted — never touched again

---

## Visual pass-by-pass

**Start:**
```
[ 64  25  12  22  11 ]
  ^--- everything unsorted
```

**Pass 1 — find min in entire array → 11 at index 4 → swap with index 0**
```
before: [ 64  25  12  22  11 ]
              scan →  →  → MIN=11
after:  [ 11 | 64  25  12  22 ]
         ✓
```

**Pass 2 — find min in [64, 25, 12, 22] → 12 at index 2 → swap with index 1**
```
before: [ 11 | 64  25  12  22 ]
                   scan →MIN=12
after:  [ 11  12 | 64  25  22 ]
         ✓   ✓
```

**Pass 3 — find min in [64, 25, 22] → 22 at index 3 → swap with index 2**
```
before: [ 11  12 | 64  25  22 ]
                   scan → MIN=22
after:  [ 11  12  22 | 64  25 ]
         ✓   ✓   ✓
```

**Pass 4 — find min in [64, 25] → 25 → swap with index 3**
```
before: [ 11  12  22 | 64  25 ]
                       scan MIN=25
after:  [ 11  12  22  25 | 64 ]
         ✓   ✓   ✓   ✓
```

**Done — last element falls into place automatically**
```
[ 11  12  22  25  64 ]
  ✓   ✓   ✓   ✓   ✓
```

---

## Java Code

```java
public static void selectionSort(int[] arr) {
    int n = arr.length;

    for (int i = 0; i < n - 1; i++) {          // i = start of unsorted section
        int minIdx = i;                          // assume first unsorted is min

        for (int j = i + 1; j < n; j++) {       // scan rest of unsorted section
            if (arr[j] < arr[minIdx]) {
                minIdx = j;                      // found a new minimum
            }
        }

        // swap minimum into position i
        int temp    = arr[i];
        arr[i]      = arr[minIdx];
        arr[minIdx] = temp;
    }
}
```

---

## What each line is doing

```
outer loop (i)  → moves the "sorted boundary" forward one step each pass
minIdx = i      → assumes current position is the minimum (will update if not)
inner loop (j)  → scans everything to the right of i
if arr[j] < arr[minIdx] → found something smaller, update minIdx
swap            → puts the true minimum at position i
```

---

## Two pointers to track mentally

```
i     = the position we're FILLING this pass (sorted boundary)
j     = the scanner, looking for the minimum
minIdx = index of the smallest value found so far
```

At the end of every pass:
- `arr[0..i]` is sorted ✓
- `arr[i+1..n-1]` is still unsorted

---

## Time & Space Complexity

| | Complexity | Why |
|---|---|---|
| Best case | O(n²) | Still scans everything even if already sorted |
| Average case | O(n²) | Always two nested loops |
| Worst case | O(n²) | Same — no early exit |
| Space | O(1) | Sorts in-place, only uses a temp variable |

> Unlike Bubble Sort, selection sort always makes exactly N-1 swaps — one per pass.
> That makes it good when swaps are expensive (like writing to flash memory).

---

## Number of operations

For array of size n:
- Pass 1 → n-1 comparisons
- Pass 2 → n-2 comparisons
- Pass 3 → n-3 comparisons
- ...
- Total = (n-1) + (n-2) + ... + 1 = **n(n-1)/2 = O(n²)**

---

## Key properties

| Property | Answer |
|---|---|
| Stable? | ❌ No (equal elements can swap order) |
| In-place? | ✅ Yes (no extra array needed) |
| Adaptive? | ❌ No (doesn't speed up on sorted input) |
| Swaps | Exactly N-1 (minimum possible) |

---

## Stable vs Unstable — why selection sort is unstable

```
arr = [ 4a  4b  1 ]   (4a and 4b are both 4, but 4a came first)

Pass 1: min = 1 at index 2. Swap with index 0.
result: [ 1  4b  4a ]   ← 4a and 4b swapped order ❌
```

If the original order of equal elements matters, use Merge Sort instead.

---

## When to use it

- ✅ Small arrays (n < 20)
- ✅ When swaps are very expensive (minimizes swaps to exactly N-1)
- ✅ Simple to implement and understand
- ❌ Not for large arrays (O(n²) is slow)
- ❌ Not when stability is needed

---

## Common Interview Questions

### Q: What's the difference between Selection Sort and Bubble Sort?
- Selection Sort: finds minimum, ONE swap per pass
- Bubble Sort: compares adjacent pairs, MANY swaps per pass
- Selection Sort does fewer writes → better when writes are costly

### Q: Can Selection Sort be made stable?
Yes — instead of swapping, shift elements one position right to insert.
But this adds complexity and defeats the simplicity of it.

### Q: Why does the outer loop go to n-1 and not n?
After n-1 passes, n-1 elements are sorted. The last element has nowhere
else to go — it's automatically the largest. No need for a final pass.

---

## One-liner to remember

> Selection sort = find minimum in unsorted section → swap to front → repeat. Always O(n²), always N-1 swaps, never stable.