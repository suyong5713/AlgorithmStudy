from collections import deque
from itertools import combinations


def bfs(virus):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    for v in virus:
        queue.append(v)
        visited[v[0]][v[1]] = 0
    last = 0
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if graph[nx][ny] == 0:
                    last = max(last, visited[nx][ny])
    cnt = 0
    for v in visited:
        cnt += v.count(-1)
    if cnt == wall:
        result.append(last)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = []
possible = []
result = []
wall = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(n):
        if graph[i][j] == 2:
            possible.append((i, j))
        if graph[i][j] == 1:
            wall += 1
for combi in combinations(possible, m):
    bfs(combi)
print(min(result) if result else -1)