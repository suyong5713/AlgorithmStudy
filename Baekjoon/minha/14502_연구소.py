from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global answer

    # graph deepcopy
    t_graph = [g[:] for g in graph]

    q = deque()
    visited = [[False] * M for _ in range(N)]

    # 바이러스가 있는 위치 큐에 넣고 방문 처리
    for i in range(N):
        for j in range(M):
            if t_graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True

    # 큐에서 하나씩 꺼내서 인접한 곳이 빈칸이면 바이러스 퍼트리기
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if t_graph[ny][nx] == 0:
                    t_graph[ny][nx] = 2
                    q.append((ny, nx))
                    visited[ny][nx] = True

    # bfs가 끝나면 안전구역 갯수 카운트 해서 현재의 안전구역 최댓값과 비교
    answer = max(answer, sum(t_graph, []).count(0))

# dfs로 벽 3개 고르기
def dfs(cnt):
    # 3개가 골라졌다면 bfs 수행해서 바이러스 퍼트리고 안전 영역 카운트
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    dfs(cnt + 1)
                    graph[i][j] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = -1

dfs(0)

print(answer)