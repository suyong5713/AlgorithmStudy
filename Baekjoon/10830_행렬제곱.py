# https://www.acmicpc.net/problem/10830
# 행렬 제곱, 분할정복

def multiply(n, matrix1, matrix2):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    
    return result

def calc(matrix1, n, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix1[i][j] %= 1000
                
        return matrix1
    elif b == 2:
        return multiply(n, matrix1, matrix1)
    else:
        matrix2 = calc(matrix1, n, b // 2)
        if b % 2 == 0:
            return multiply(n, matrix2, matrix2)
        else:
            return multiply(n, multiply(n, matrix2, matrix2), matrix1)

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

result = calc(a, n, b)
for r in result:
    print(*r)
