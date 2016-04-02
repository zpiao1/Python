def squareMatrixMultiply(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(0)
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(squareMatrixMultiply(A, B))
# [[19, 22], [43, 50]]

