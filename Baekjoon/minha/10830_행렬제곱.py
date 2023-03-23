def matrix(a, b):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][k] += a[i][j] * b[j][k] % 1000 # 안 나눠주니까 시간 초과 나더라..

    return res

def divide(n, mat):
    if n == 1:
        return mat
    else:
        d_mat = divide(n // 2, mat)
        if n % 2 == 0:
            return matrix(d_mat, d_mat)
        else:
            return matrix(matrix(d_mat, d_mat), mat)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

answer = divide(B, A)

for row in answer:
    for col in row:
        print(col % 1000, end=' ')
    print()