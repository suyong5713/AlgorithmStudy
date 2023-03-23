from collections import deque


def BFS(row, col):
    queue = deque()
    queue.append([row, col])
    while queue:
        row, col = queue.popleft()
        for dir in range(4):
            n_row = row + d_row[dir]
            n_col = col + d_col[dir]
            if 0 <= n_row < N and 0 <= n_col < M:
                # 치즈 일때
                if grid[n_row][n_col] == 1:
                    visited[n_row][n_col] += 1
                # 치즈 아닐때
                else:
                    if not visited[n_row][n_col]:
                        visited[n_row][n_col] = 1
                        queue.append([n_row, n_col])
    return


def melt():
    melt_count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                grid[i][j] = 0
                melt_count += 1
    if melt_count > 0:
        return True
    else:
        return False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
d_row = [1, -1, 0, 0]
d_col = d_row[::-1]
time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = True
    BFS(0, 0)
    if not melt():
        break
    time += 1
print(time)