def solution(n, results):
    rank = [[0] * n for _ in range(n)]

    for A, B in results:
        rank[A - 1][B - 1] = 1
        rank[B - 1][A - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and rank[i][j] == 0:
                    if rank[i][k] == 1 and rank[k][j] == 1:
                        rank[i][j] = 1
                    elif rank[i][k] == -1 and rank[k][j] == -1:
                        rank[i][j] = -1

    answer = 0
    for r in range(n):
        if rank[r].count(0) == 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))