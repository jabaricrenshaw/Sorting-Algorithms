def QuickSort(arr, start_idx, end_idx):
    if start_idx >= end_idx:
        return arr
    
    midpoint = Partition(arr, start_idx, end_idx)

    QuickSort(arr, start_idx, midpoint - 1)
    QuickSort(arr, midpoint + 1, end_idx)

    return arr

def Partition(arr, start_idx, end_idx):
    pivot = arr[end_idx]
    i = start_idx - 1

    for j in range(start_idx, end_idx):
        if arr[j] <= pivot:
            Swap(arr, j, i+1)
            i += 1
    Swap(arr, end_idx, i+1)
    return i+1

def Swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp



if __name__ == "__main__":
    arr = [6, 1, 0, 2, 9, 3, 8, 4, 7, 5]
    print("Quick:", QuickSort(arr, 0, len(arr) - 1))
