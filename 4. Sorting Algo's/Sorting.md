## Quick Comparison
 
| Property | Bubble Sort | Insertion Sort |
|----------|-------------|----------------|
| Best case | O(n) | O(n) |
| Average | O(n²) | O(n²) |
| Worst case | O(n²) | O(n²) |
| Stable? | ✅ Yes | ✅ Yes |
| Adaptive? | ✅ Yes (with flag) | ✅ Yes (naturally) |
| Swaps per pass | Many (adjacent only) | At most 1 insert per pass |
| Good for nearly-sorted data? | Yes | **Better** |
| Intuition | Bubbles max to right | Cards in hand |
 
> **Insertion sort is generally faster in practice** for small or nearly-sorted arrays because it does fewer comparisons and moves data more efficiently.
 
---
 
## When to use which
 
- **Bubble sort** — teaching/demo purposes. Rarely used in production.
- **Insertion sort** — small arrays (< ~20 elements), nearly-sorted data, or as the base case inside hybrid sorts like Timsort (Python's built-in sort uses it).
- **Neither** — for large unsorted arrays, use Merge Sort O(n log n) or Quick Sort O(n log n) average.
