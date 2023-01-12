from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sty, stx, dey, dex):
    q = deque()
    visited = [[False] * N for _ in range(N)]

    # 시작 지점과 초기 거리(0) 넣기
    q.append((sty, stx, 0))
    visited[sty][stx] = True

    while q:
        cy, cx, dis = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 범위내에 방문하지 않은 벽이 아닌 지점에 대해
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] != 1:
                # 목적지이면 거리 리턴
                if ny == dey and nx == dex:
                    return dis + 1
                else:
                    q.append((ny, nx, dis + 1))
                    visited[ny][nx] = True


def find_target():
    min_dis = 1e9
    # 최솟값인 승객 정보 담는 리스트
    cus = []
    # 승객 한명씩 확인하며 아직 완료되지 않은 경우 현재 택시 위치에서부터 승객까지의 거리 구함
    for i in range(M):
        if not done[i]:
            i_dis = bfs(ty, tx, cus_start[i][0], cus_start[i][1])
            # 갈 수 있는 길이 없으면 다음 반복문 탐색
            if i_dis is None:
                continue
            # 더 짧다면 최솟값 갱신하고 cus 비우기
            if i_dis < min_dis:
                min_dis = i_dis
                cus.clear()
                cus.append((i, cus_start[i][0], cus_start[i][1]))
            # 거리가 같다면 cus에 승객 번호와 승객의 위치 정보 넣기
            elif i_dis == min_dis:
                cus.append((i, cus_start[i][0], cus_start[i][1]))

    # 갈 수 있는 길이 없으면 -1 리턴
    if len(cus) == 0:
        return -1, -1

    # 최소 거리인 승객이 1명 이상이면 행>열 순서로 정렬
    if len(cus) > 1:
        cus.sort(key=lambda x: (x[1], x[2]))

    # 타겟 승객의 번호와 그 승객까지의 거리 리턴
    return cus[0][0], min_dis


N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ty, tx = map(int, input().split())
ty -= 1
tx -= 1

# 승객의 위치와 승객의 목적지 저장
cus_start = []
cus_des = []
for _ in range(M):
    csy, csx, cdy, cdx = map(int, input().split())
    cus_start.append((csy - 1, csx - 1))
    cus_des.append((cdy - 1, cdx - 1))

# idx - 1번 승객의 완료 여부
done = [False] * M
# 모든 승객 다 완료되었을 때 True로 바뀌는 플래그 -> 연료 0일 때 다 끝나기 전인지 후인지 확인하기 위해
flag = False

while True:
    # 모든 승객이 완료되었다면 반복문 탈출
    if done.count(True) == M:
        flag = True
        break
    # 모든 승객이 완료 안되었는데 연료양 0이면 반복문 탈출
    if fuel == 0:
        break

    # 가장 짧은 거리의 승객 번호와 거리 구하기
    target_idx, target_dis = find_target()

    if target_idx == -1:
        fuel = 0
        break

    # 택시 위치 타겟 승객의 위치로 변경
    ty, tx = cus_start[target_idx]
    # 연료 소모 후 양 체크
    fuel -= target_dis
    if fuel < 0:
        break

    # 승객의 위치 ~ 목적지 위치 최단 거리 구하기
    cus_dis = bfs(cus_start[target_idx][0], cus_start[target_idx][1], cus_des[target_idx][0], cus_des[target_idx][1])
    # 택시 위치 타겟 승객의 목적지 위치로 변경
    ty, tx = cus_des[target_idx]
    # 연료 소모 후 양 체크, 0 이상이면 연료 충전 후 승객 완료 여부 변경
    fuel -= cus_dis
    if fuel < 0:
        break
    else:
        fuel += 2 * cus_dis
        done[target_idx] = True

if fuel == 0:
    if flag:
        print(0)
    else:
        print(-1)
elif fuel < 0:
    print(-1)
else:
    print(fuel)