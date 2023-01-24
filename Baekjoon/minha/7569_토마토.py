from collections import deque

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i, j, k, 0))

while q:
    cz, cy, cx, day = q.popleft()
    for i in range(6):
        nz = cz + dz[i]
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0:
            box[nz][ny][nx] += 1
            q.append((nz, ny, nx, day + 1))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit()

print(day)