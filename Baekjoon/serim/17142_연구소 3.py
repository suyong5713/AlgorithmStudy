from collections import deque
from itertools import combinations


def bfs(virus):
    # 방문 처리와 시간 확인을 한 곳에서 처리
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    # 방문한 좌표의 visited 값을 0으로 변경, queue에 바이러스 위치 추가
    for v in virus:
        queue.append(v)
        visited[v[0]][v[1]] = 0
    last = 0
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                # 비활성이 활성화되는 최종 시간을 확인
                if graph[nx][ny] == 0:
                    last = max(last, visited[nx][ny])
    cnt = 0
    for v in visited:
        cnt += v.count(-1)
    # 방문 안한 좌표 수 == 벽의 수 => 벽 제외 모든 좌표에 바이러스 퍼뜨림
    if cnt == wall:
        result.append(last)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 연구소의 크기, 놓을 수 있는 바이러스의 개수
n, m = map(int, input().split())
graph = []
# 바이러스를 놓을 수 있는 위치
possible = []
result = []
wall = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(n):
        # 바이러스를 놓을 수 있는 위치
        if graph[i][j] == 2:
            possible.append((i, j))
        # 벽의 위치
        if graph[i][j] == 1:
            wall += 1
# m개의 바이러스를 조합으로 선정하여 해당 조합에 대해 탐색
for combi in combinations(possible, m):
    bfs(combi)
print(min(result) if result else -1)