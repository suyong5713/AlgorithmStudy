from collections import deque

def east():
    dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
    end = dice[1][2]
    for i in range(2, 0, -1):
        dice[1][i] = dice[1][i - 1]
    dice[1][0] = end

def west():
    dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
    end = dice[1][0]
    for i in range(0, 2):
        dice[1][i] = dice[1][i + 1]
    dice[1][2] = end


def south():
    end = dice[3][1]
    for i in range(3, 0, -1):
        dice[i][1] = dice[i-1][1]
    dice[0][1] = end

def north():
    end = dice[0][1]
    for i in range(0, 3):
        dice[i][1] = dice[i+1][1]
    dice[3][1] = end

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    cnt = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == graph[y][x] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1

    return cnt


N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]

cy, cx = 0, 0
# 동 -> 남 -> 서 -> 북 : 처음에 동쪽, 시계 방향
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
curd = 0

score = 0

for _ in range(K):
    if not(0 <= cy + dy[curd] < N and 0 <= cx + dx[curd] < M):
        if curd < 2:
            curd += 2
        else:
            curd -= 2

    cy += dy[curd]
    cx += dx[curd]

    if curd == 0:
        east()
    elif curd == 1:
        south()
    elif curd == 2:
        west()
    else:
        north()

    B = graph[cy][cx]
    C = bfs(cy, cx)

    score += (B * C)

    A = dice[3][1]

    if A > B:
        if curd < 3:
            curd += 1
        else:
            curd = 0
    elif A < B:
        if curd > 0:
            curd -= 1
        else:
            curd = 3

print(score)