def three_way_partition(arr, a, b):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif a <= arr[mid] <= b:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


arr = [1, 2, 3, 3, 4]
a, b = 1, 2
print(three_way_partition(arr, a, b))