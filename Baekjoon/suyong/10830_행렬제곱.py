def matrix_mul(matrix1, matrix2):
    result_matrix = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            sub_sum = 0
            for k in range(N):
                sub_sum += matrix1[row][k] * matrix2[k][col]
            result_matrix[row][col] = sub_sum % 1000
    return result_matrix


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = [[] for _ in range(N)]
for i in range(N):
    answer[i] = A[i][:]

binary = bin(B)[2:]
for i in range(1, len(binary)):
    if binary[i] == "1":
        answer = matrix_mul(matrix_mul(answer, answer), A)
    else:
        answer = matrix_mul(answer, answer)

for row in answer:
    print(*row)