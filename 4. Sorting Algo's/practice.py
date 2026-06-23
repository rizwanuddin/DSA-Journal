def SelectionSort(arr):
    l = len(arr)
    for i in range(l-1):
        minidx = i
        for j in range(i+1, l):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]



def InsertionSort():
    l = len(arr)
    for i in range(1,l):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


def BubbleSort():
    l = len(arr)
    for i in range(l - 1):
        swapped = False
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True        
        if not swapped :
            break        



arr = [2,7,8,5,4,1]
