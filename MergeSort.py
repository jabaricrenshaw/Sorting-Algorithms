def Merge_Sort(arr, start_idx, end_idx):
    if start_idx == end_idx:
        return

    midpoint = (start_idx + end_idx)//2
    # Left Subarray
    Merge_Sort(arr, start_idx, midpoint)
    # Right Subarray
    Merge_Sort(arr, midpoint + 1, end_idx)
    # Merge two Subarrays
    Merge(arr, start_idx, midpoint, end_idx)

    return arr


def Merge(arr, start_idx, midpoint, end_idx):
    # Create two temp arrays
    # Left of size
    # Right of size
    left_size = (midpoint - start_idx + 1)
    right_size = (end_idx - midpoint)

    left_arr = [0] * (left_size + 1)
    right_arr = [0] * (right_size + 1)

    i = j = 0
    for k in range(start_idx, end_idx + 1):
        if k <= midpoint:
            left_arr[i] = arr[k]
            i+=1
        elif k > midpoint:
            right_arr[j] = arr[k]
            j+=1

    large = max(left_arr[left_size - 1], right_arr[right_size - 1]) + 1

    left_arr[left_size] = large
    right_arr[right_size] = large

    i = j = 0
    for k in range(start_idx, end_idx + 1):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


if __name__ == "__main__":
    arr3 = [6, 1, 0, 2, 9, 3, 8, 4, 7, 5]
    print("Merge:", Merge_Sort(arr3, 0, len(arr3)-1))
