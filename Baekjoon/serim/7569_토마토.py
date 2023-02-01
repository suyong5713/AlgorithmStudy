from collections import deque


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for dir in range(6):
            nx = x + dx[dir]
            ny = y + dy[dir]
            nz = z + dz[dir]
            # 범위 안에 있으며 익지 않은 토마토의 경우
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                # 큐에 추가 / 해당 배열 값을 이전 배열 값보다 1 크게 저장 (1일이 지남)
                queue.append([nx, ny, nz])
                graph[nx][ny][nz] = graph[x][y][z] + 1


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
day = 0
queue = deque()
# 익은 토마토들의 좌표를 큐에 미리 넣어줌
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

for i in graph:
    for j in i:
        for k in j:
            # 익지 않은 토마토가 있을 경우
            if k == 0:
                print(-1)
                exit(0)
        # 최대일수가 현재 날짜
        day = max(day, max(j))

print(day - 1)