from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    cnt = 0

    q = deque()
    q.append((0, 0))
    visited = [[0] * W for _ in range(H)]

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < H and 0 <= nx < W:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                if graph[ny][nx] == 1 and visited[ny][nx] < 2:
                    visited[ny][nx] += 1
                    if visited[ny][nx] == 2:
                        graph[ny][nx] = 0
                        cnt += 1

    return cnt

H, W = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
time = 0

while True:
    melt = bfs()
    if not melt:
        break
    else:
        time += 1

print(time)