def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            temp = arr[i]
            j = i - 1
            while temp <= arr[j] and j >= 0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
    
    return arr
            
                



if __name__ == "__main__":
    arr = [6, 1, 0, 2, 9, 3, 8, 4, 7, 5]
    print("Insertion:", Insertion_Sort(arr))
