def DFS(depth):
    global answer
    if depth == N:
        answer += 1
        return

    for i in range(N):
        row[depth] = i
        if check(depth):
            DFS(depth + 1)


def check(depth):
    for i in range(depth):
        if row[depth] == row[i] or abs(row[depth] - row[i]) == depth - i:
            return False
    return True


N = int(input())
board = [[0] * N for _ in range(N)]
answer = 0
row = [0] * N
DFS(0)
print(answer)
