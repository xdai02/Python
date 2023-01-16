N = 3

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
C = []

for i in range(N):
    C.append([])
    for j in range(N):
        C[i].append(0)
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]

for i in range(N):
    for j in range(N):
        print(C[i][j], end=' ')
    print()