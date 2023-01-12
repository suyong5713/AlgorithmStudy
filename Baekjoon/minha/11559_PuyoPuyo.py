from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x, color):
    q = deque()
    visited = [[False] * 6 for _ in range(12)]

    q.append((y, x))
    visited[y][x] = True

    same = []
    same.append((y, x))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and field[ny][nx] == color:
                q.append((ny, nx))
                visited[ny][nx] = True
                same.append((ny, nx))

    if len(same) >= 4:
        return same
    else:
        return []


field = [list(map(str, input().strip())) for _ in range(12)]

answer = 0
while True:
    targets = []
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] in ['R', 'G', 'B', 'P', 'Y']:
                target = bfs(i, j, field[i][j])
                if len(target) > 0:
                    for t in target:
                        targets.append(t)

    if len(targets) == 0:
        break

    answer += 1

    for ty, tx in targets:
        field[ty][tx] = 'X'

    c_field = []
    for col in reversed(list(map(list, zip(*field)))):
        n_col = deque([i for i in col if i != 'X'])
        for _ in range(12 - len(n_col)):
            n_col.appendleft('.')

        c_field.append(n_col)

    field = list(map(list, zip(*c_field)))

print(answer)