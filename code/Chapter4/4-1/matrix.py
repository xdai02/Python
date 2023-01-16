A = [
    [1, 3],
    [1, 0],
    [1, 2]
]

B = [
    [0, 0],
    [7, 5],
    [2, 1]
]

C = []
print("Matrix Addition")
for i in range(3):
    C.append([])
    for j in range(2):
        C[i].append(A[i][j] + B[i][j])
        print("%3d" % C[i][j], end='')
    print()

C = []
print("Matrix Subtraction")
for i in range(3):
    C.append([])
    for j in range(2):
        C[i].append(A[i][j] - B[i][j])
        print("%3d" % C[i][j], end='')
    print()