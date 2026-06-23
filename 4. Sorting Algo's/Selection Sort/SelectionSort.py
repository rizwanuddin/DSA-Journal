def maxselectionsort(arr):






    pass
def minselectionsort(arr):
    l = len(arr) 
    for i in range(l - 1):
        minidx = i
        for curr in range(i + 1, l):
            if arr[curr] < arr[minidx]:
                minidx = curr
        arr[i], arr[minidx] = arr[minidx], arr[i]
        """ 
        we write it this way in java Because Java does not support Python-style multiple assignment.
        temp = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = temp
        """


arr = [9,5,2,8,1]
minselectionsort(arr)
print(arr)  
"""
class SelectionSort:
    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    sorter = SelectionSort()

    sorted_arr = sorter.selection_sort(arr)

    for num in sorted_arr:
        print(num, end=" ")
"""