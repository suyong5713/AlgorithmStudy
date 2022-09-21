from collections import deque


def find_group(y, x, color):
    # bfs로 주변 좌표 탐색하며
    # 일반 블록인 경우 방문처리, block_cnt 증가, blocks에 좌표 넣기
    # 무지개 블록인 경우 방문처리, block_cnt와 rainbow_cnt 모두 증가, blocks와 rainbows에 좌표 넣기
    q = deque()
    q.append((y, x))

    block_cnt, rainbow_cnt = 1, 0
    blocks = [(y, x)]
    rainbows = []

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if graph[ny][nx] == color:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    block_cnt += 1
                    blocks.append((ny, nx))
                elif graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    block_cnt += 1
                    rainbow_cnt += 1
                    blocks.append((ny, nx))
                    rainbows.append((ny, nx))

    # 무지개 블록은 여러 블록 그룹에서 중복해서 방문할 수 있기 때문에 방문처리 해제
    for ry, rx in rainbows:
        visited[ry][rx] = False

    # 그룹의 블록 총 개수와, 무지개 블록 개수, 그룹의 블록 좌표 리스트 리턴
    return block_cnt, rainbow_cnt, blocks

# 블록 그룹에 속한 블록들의 좌표를 받아와 값을 -2로 설정해주고, 그룹의 크기를 리턴
def remove(block_group):
    for y, x in block_group:
        graph[y][x] = -2

    return len(block_group)

# 각 열별로 행을 거꾸로 탐색하며
def gravity():
    for c in range(0, N):
        for r in range(N - 2, -1, -1):
            # 좌표가 -1보다 큰 경우(일반 블록이나 무지개 블록인 경우)
            if graph[r][c] > -1:
                # 해당 행을 타겟으로 잡기
                target = r
                while True:
                    # 타겟에서 아래쪽으로 한칸씩 내려가면서 이동한 곳이 범위내에 존재하고, 빈 공간이면 값 갱신
                    if 0 <= target + 1 < N and graph[target + 1][c] == -2:
                        graph[target + 1][c] = graph[target][c]
                        graph[target][c] = -2
                        target += 1
                    # 아니면 while문 탈출
                    else:
                        break


# 0921.md 참고
def rotation():
    res = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            res[N-j-1][i] = graph[i][j]

    return res


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
score = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while True:
    # 한 번의 오토 플레이가 끝나면 방문 배열, 가능한 블럭 그룹 리스트 초기화
    visited = [[False] * N for _ in range(N)]
    group = []

    # 그래프를 탐색하며 어떤 지점이 방문하지 않았고, 일반 블럭이 있다면 방문처리, 인접한 그룹 찾기
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > 0:
                visited[i][j] = True
                adj = find_group(i, j, graph[i][j]) # 인접한 그룹을 찾아 그룹에 속한 블럭의 수, 무지개 블럭의 수, 그룹에 속한 블럭들의 좌표값을 리턴 받는다
                if adj[0] >= 2: # 그룹에 속한 블럭의 수가 2보다 크면 가능한 블럭 그룹 리스트에 해당 정보를 넣는다
                    group.append(adj)

    # 가능한 블럭 그룹 리스트 정렬
    group.sort(reverse=True)

    # 가능한 블럭이 없다면 반복문 탈출
    if len(group) == 0:
        break

    # 크기가 가장 큰 블럭 그룹에 속한 블럭을 지우고 점수값을 리턴 받아 현재 점수에 더해준다
    s = remove(group[0][2])
    score += pow(s, 2)

    # 중력 -> 회전 -> 중력
    gravity()
    graph = rotation()
    gravity()

# while문 탈출하면 점수 출력
print(score)