from collections import deque

# east, west, south, north -> 주사위 전개도 바꾸는 함수
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

# bfs 탐색으로 같은 값을 가진 좌표의 갯수 리턴
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
# 현재 방향
curd = 0

score = 0

for _ in range(K):
    # 다음 위치가 범위를 벗어날 경우 반대 방향으로 바꿔주기
    if not(0 <= cy + dy[curd] < N and 0 <= cx + dx[curd] < M):
        if curd < 2:
            curd += 2
        else:
            curd -= 2

    # 다음 위치 갱신
    cy += dy[curd]
    cx += dx[curd]

    # 주사위 전개도 바꿔주기
    if curd == 0:
        east()
    elif curd == 1:
        south()
    elif curd == 2:
        west()
    else:
        north()

    # B는 해당 위치의 값, C는 값이 같아 연속해서 이동할 수 있는 칸의 수
    B = graph[cy][cx]
    C = bfs(cy, cx)
    # 점수 더해주기
    score += (B * C)

    # A는 주사위 아랫면의 숫자
    A = dice[3][1]

    # 숫자 비교해서 이동 방향 갱신
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