#special traversing a matrix
def spiral_order(matrix):
    res = []
    while matrix:
        res += list(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]
    return res

# Example from sheet: 4x4 matrix
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(spiral_order(mat))