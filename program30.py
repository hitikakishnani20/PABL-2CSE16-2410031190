#FIND MEDIAN IN AN ARRAY
def find_median(arr):
    # Step 1: Sort the array
    arr.sort()
    n = len(arr)

    # Step 2: Check odd or even
    if n % 2 == 1:           # odd
        return arr[n // 2]
    else:                    # even
        return (arr[n//2 - 1] + arr[n//2]) / 2


# Examples
arr1 = [90, 100, 78, 89, 67]
print(find_median(arr1))   # 89

arr2 = [56, 67, 30, 79]
print(find_median(arr2))   # 61.5

arr3 = [1, 2]
print(find_median(arr3))   # 1.5