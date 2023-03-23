def backtracking(cy, cx, cnt):
    global answer

    answer = max(answer, cnt)

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] not in visited_alpha:
                visited_alpha.add(board[ny][nx])
                backtracking(ny, nx, cnt + 1)
                visited_alpha.remove(board[ny][nx])

R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited_alpha = set()

answer = -1

visited_alpha.add(board[0][0])
backtracking(0, 0, 1)

print(answer)