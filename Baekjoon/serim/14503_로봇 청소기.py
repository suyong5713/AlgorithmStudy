import sys
sys.stdin = open("input.txt", "r")

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
# d => 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문 기록 배열
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
# 청소하는 칸
cnt = 1
# 회전 횟수
turn_time = 0
while True:
    # 반시계 방향으로 회전
    d -= 1
    if d == -1:
        d = 3
    nx = r + dx[d]
    ny = c + dy[d]
    # 방문하지 않았고 벽도 아닐 경우
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        r = nx
        c = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 모든 방향을 회전했을 경우
    if turn_time == 4:
        # 후진
        nx = r - dx[d]
        ny = c - dy[d]
        # 후진한 곳을 청소할 수 있을 경우 이동
        if graph[nx][ny] == 0:
            r = nx
            c = ny
        # 벽이거나 청소되어 있을 경우 작동 멈춤
        else:
            break
        turn_time = 0

print(cnt)