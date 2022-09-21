import sys
sys.stdin = open("input.txt", "r")

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

up = 0
down = 0
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                amount = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        temp[nx][ny] += arr[i][j] // 5
                        amount += arr[i][j] // 5
                arr[i][j] -= amount

    for i in range(r):
        for j in range(c):
            arr[i][j] += temp[i][j]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)
