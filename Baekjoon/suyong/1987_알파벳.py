import sys
def dfs(row, col, depth):
    global answer
    for dir in range(4):
        n_row = row + d_row[dir]
        n_col = col + d_col[dir]
        if 0 <= n_row < R and 0 <= n_col < C and not board[n_row][n_col] in history:
            history.add(board[n_row][n_col])
            dfs(n_row, n_col, depth + 1)
            history.remove(board[n_row][n_col])
    else:
        answer = max(depth, answer)
    return

answer = 0
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
history = set()
history.add(board[0][0])
dfs(0, 0, 1)
print(answer)
print()

