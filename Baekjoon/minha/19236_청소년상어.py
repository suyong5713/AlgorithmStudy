import copy

def fish(sy, sx, cgraph):
    # 1번부터 16번 물고기에 대해 위치 구하기
    for num in range(1, 17):
        fy, fx = -1, -1
        flag = False
        for i in range(4):
            for j in range(4):
                if cgraph[i][j][0] == num:
                    fy, fx = i, j
                    flag = True
                    break
            if flag:
                break

        # 존재하지 않는 물고기면 다음 물고기 탐색
        if fy == -1 and fx == -1:
            continue

        # 존재하면 물고기의 방향 구하기
        fd = cgraph[fy][fx][1]

        # 물고기가 이동할 수 있는 방향을 찾고 이동시킴
        for _ in range(7):
            ny = fy + dy[fd]
            nx = fx + dx[fd]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if ny != sy or nx != sx:
                    cgraph[fy][fx], cgraph[ny][nx] = cgraph[ny][nx], cgraph[fy][fx]
                    cgraph[ny][nx][1] = fd
                    break
            fd = (fd + 1) % 8


def shark(sy, sx, cgraph):
    candidate = []
    # 상어의 방향 구하기
    sd = cgraph[sy][sx][1]

    # 4x4 크기이므로 최대 3칸 이동 가능
    # 이동 방향으로 한칸씩 이동하면서 이동이 가능한 곳이고, 물고기가 있으면 이동 가능한 자리 리스트에 넣기
    for i in range(3):
        sy += dy[sd]
        sx += dx[sd]

        if 0 <= sy < 4 and 0 <= sx < 4:
            if 0 < cgraph[sy][sx][0] <= 16:
                candidate.append((sy, sx))

    return candidate


def dfs(sy, sx, score, cgraph):
    global answer

    # 각각의 가능한 경우에 재귀 돌기 위해 딥카피
    cgraph = copy.deepcopy(cgraph)

    # 물고기 번호 합 갱신하고 잡아먹힌 물고기 자리의 값 0으로 바꾸기
    score += cgraph[sy][sx][0]
    cgraph[sy][sx][0] = 0

    # 최댓값 확인
    answer = max(answer, score)

    # 물고기 이동
    fish(sy, sx, cgraph)

    # 상어가 이동 가능한 자리 구하고 각각의 자리 재귀함수
    candidate = shark(sy, sx, cgraph)
    for cy, cx in candidate:
        dfs(cy, cx, score, cgraph)


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[] for _ in range(4)]

# 입력 정보를 (물고기 번호, 방향)으로 묶기
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        graph[i].append([tmp[2 * j], tmp[2 * j + 1] - 1])

answer = 0
dfs(0, 0, 0, graph)

print(answer)