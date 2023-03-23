from collections import deque


def bfs():
    # 치즈가 존재하는지 판단하기 위한 flag
    global flag
    # 매번의 bfs마다 방문처리와 치즈 개수를 확인하는 리스트는 초기화
    visited = [[0] * m for _ in range(n)]
    cheese = [[0] * m for _ in range(n)]
    # 공기의 좌표를 넣을 queue
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 공기(0)
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
            # 치즈(1)
            if 1 <= nx < n - 1 and 1 <= ny < m - 1 and graph[nx][ny] == 1:
                cheese[nx][ny] += 1
                flag = True
    # 두 면 이상의 공기 접촉이 있는 치즈에 대해 삭제
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 2:
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = 0    # 시간

while True:
    flag = False
    bfs()
    result += 1
    # 남은 치즈가 없으면 break
    if not flag: break

print(result - 1)