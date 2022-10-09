def backtracking(y, x, cnt, cur):
    global res

    if cnt == 4:
        res = max(res, cur)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            backtracking(ny, nx, cnt + 1, cur + graph[ny][nx])
            visited[ny][nx] = False

def threeWay(y, x):
    global res

    if x + 2 < M and y + 1 < N:
        down = [graph[y][x], graph[y][x + 1], graph[y][x + 2], graph[y + 1][x + 1]]
        res = max(res, sum(down))
    if x + 1 < M and y + 2 < N:
        right = [graph[y][x], graph[y + 1][x], graph[y + 2][x], graph[y + 1][x + 1]]
        res = max(res, sum(right))
    if x + 2 < M and y - 1 >= 0:
        up = [graph[y][x], graph[y][x + 1], graph[y][x + 2], graph[y - 1][x + 1]]
        res = max(res, sum(up))
    if x - 1 >= 0 and y + 2 < N:
        left = [graph[y][x], graph[y + 1][x], graph[y + 2][x], graph[y + 1][x - 1]]
        res = max(res, sum(left))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = -1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        backtracking(i, j, 1, graph[i][j])
        visited[i][j] = False
        threeWay(i, j)

print(res)