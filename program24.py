def min_swaps(arr, k):
    count = 0
    for i in arr:
        if i <= k:
            count += 1

    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    ans = bad
    j = count

    for i in range(len(arr)):
        if j == len(arr):
            break
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        ans = min(ans, bad)
        j += 1

    return ans


arr = [2, 1, 5, 6, 3]
k = 3
print(min_swaps(arr, k))