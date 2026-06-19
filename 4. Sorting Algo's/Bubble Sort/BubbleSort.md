
 
## Bubble Sort
 
### Concept
Repeatedly scan adjacent pairs. If they're out of order, swap them. After each pass, the largest unsorted element "bubbles" to its correct position at the right end.
 
### Complexity
|Case | Time | Space |
|------|------|-------|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |
 
> **Best case is O(n)** only with the early-exit flag. Without it, it's always O(n²).
 
### Java
 
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
 
### Python
 
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        sorted_flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False
        if not sorted_flag:
            break
```
 
> Note: The Python version uses `break` for brevity. For a loop-invariant-friendly version, use a `while` loop with the flag in the condition (see CS 146 notes).
 
### Loop Invariant
After pass `i`, the last `i` elements are in their final sorted positions.
 

