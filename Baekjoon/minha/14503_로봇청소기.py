N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 0: 북, 1: 동, 2: 남, 3: 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited[r][c] = True
cnt = 1

while True:
    clean = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = c + dx[d]
        ny = r + dy[d]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                r, c = ny, nx
                clean = True
                break
    if not clean:
        if graph[r-dy[d]][c-dx[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dy[d], c-dx[d]