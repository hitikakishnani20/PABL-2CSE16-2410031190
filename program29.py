def first_one(row):
    left, right = 0, len(row) - 1
    pos = len(row)

    while left <= right:
        mid = (left + right) // 2
        if row[mid] == 1:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1
    return pos


def row_with_max_ones(arr):
    max_ones = 0
    index = -1
    m = len(arr[0])

    for i in range(len(arr)):
        first = first_one(arr[i])
        ones = m - first

        if ones > max_ones:
            max_ones = ones
            index = i

    return index


# Example
arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(row_with_max_ones(arr))   # 2