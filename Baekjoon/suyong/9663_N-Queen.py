N = int(input())
board = [[0] * N for _ in range(N)]
answer = 0
def check(x, y):
    for i in range(N):
        if board[x][i] == 1:
            return False
        if board[i][y] == 1:
            return False
    for i in range(N):
        for j in range(N):
            if abs(x - i) == abs(y - j):
                if board[i][j] == 1:
                    return False
    return True
def dfs(cnt):
    global answer
    if cnt == N:
        answer += 1
        return
    for i in range(N):
        if check(cnt, i):
            board[cnt][i] = 1
            dfs(cnt + 1)
            board[cnt][i] = 0

dfs(0)
print(answer)
