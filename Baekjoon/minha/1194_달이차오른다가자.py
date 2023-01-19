from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    q = deque()
    visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]

    q.append((sy, sx, 0, 0))
    visited[sy][sx][0] = True

    while q:
        cy, cx, cnt, key = q.popleft()
        if graph[cy][cx] == '1':
            return cnt
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][key] and graph[ny][nx] != '#':
                if graph[ny][nx].islower():
                    tmp_key = key | (1 << (ord(graph[ny][nx]) - ord('a')))
                    visited[ny][nx][tmp_key] = True
                    q.append((ny, nx, cnt + 1, tmp_key))
                elif graph[ny][nx].isupper():
                    if key & (1 << (ord(graph[ny][nx]) - ord('A'))):
                        visited[ny][nx][key] = True
                        q.append((ny, nx, cnt + 1, key))
                else:
                    visited[ny][nx][key] = True
                    q.append((ny, nx, cnt + 1, key))

    return -1


N, M = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(N)]

start = []
flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            graph[i][j] = '.'
            start.append((i, j))
            flag = True
            break
    if flag:
        break

print(bfs(start[0][0], start[0][1]))