from collections import deque


def bfs(y, x, cur_size):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((y, x, 0))
    visited[y][x] = True
    candidate = []

    while q:
        cy, cx, dis = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                if 0 < graph[ny][nx] < cur_size:
                    candidate.append((ny, nx, dis + 1))
                    q.append((ny, nx, dis + 1))
                elif graph[ny][nx] == 0 or graph[ny][nx] == cur_size:
                    q.append((ny, nx, dis + 1))

    if candidate:
        candidate.sort(key=lambda x: (x[2], x[0], x[1]))
        return candidate[0][0], candidate[0][1], candidate[0][2]

    return -1, -1, -1


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
sy, sx = -1, -1
size = 2
eat = 0
answer = 0

for i in range(N):
    flag = False
    for j in range(N):
        if graph[i][j] == 9:
            sy, sx = i, j
            graph[i][j] = 0
            flag = True
            break
    if flag:
        break

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while True:
    y, x, time = bfs(sy, sx, size)
    if y == -1 or x == -1 or time == -1:
        break
    else:
        graph[y][x] = 0
        eat += 1
        answer += time
        if eat == size:
            size += 1
            eat = 0
        sy, sx = y, x

print(answer)