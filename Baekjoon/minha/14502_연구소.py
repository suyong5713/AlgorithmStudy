from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global answer

    t_graph = [g[:] for g in graph]

    q = deque()
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if t_graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if t_graph[ny][nx] == 0:
                    t_graph[ny][nx] = 2
                    q.append((ny, nx))
                    visited[ny][nx] = True

    answer = max(answer, sum(t_graph, []).count(0))

def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    dfs(cnt + 1)
                    graph[i][j] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = -1

dfs(0)

print(answer)