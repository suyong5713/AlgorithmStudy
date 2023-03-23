from itertools import combinations
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(comb):
    q = deque()
    visited = [[-1] * N for _ in range(N)]

    for y, x in comb:
        q.append((y, x))
        visited[y][x] = 0

    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and lab[ny][nx] != 1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[cy][cx] + 1

    for i, j in virus:
        if (i, j) not in comb:
            visited[i][j] = 0

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0 and visited[i][j] == -1:
                return 1e9

    return max(map(max, visited))

N, M = map(int, input().split())
answer = 1e9

lab = []
virus = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 2:
            virus.append((r, c))
    lab.append(row)

for comb in combinations(virus, M):
    res = bfs(comb)
    if res != -1e9:
        answer = min(answer, res)

if answer == 1e9:
    print(-1)
else:
    print(answer)