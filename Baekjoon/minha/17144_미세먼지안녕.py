from collections import deque


def spread():
    # 확산이 동시에 모든 칸에서 발생하므로 크기가 RxC인 s에 증감값 저장
    s = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # A의 모든 칸을 돌면서 미세먼지가 존재하면
            if A[i][j] > 0:
                cnt = 0
                for k in range(4):
                    adj_y, adj_x = i + dy[k], j + dx[k]
                    # 상하좌우 4곳이 범위 내에 있고 공기청정기가 있는 곳이 아니라면
                    # 증감값에 A[i][j]//5 더하고, 확산된 방향의 개수 증가
                    if 0 <= adj_y < R and 0 <= adj_x < C and A[adj_y][adj_x] != -1:
                        s[adj_y][adj_x] += A[i][j]//5
                        cnt += 1
                # 상하좌우 4곳 탐색을 마치면 증감값에 A[i][j]//5*cnt 빼기
                s[i][j] -= A[i][j]//5*cnt

    # 모든 좌표를 탐색했다면
    # A에 증감값 더해줌
    for i in range(R):
        for j in range(C):
            A[i][j] += s[i][j]


def air_cleaner():
    # 공기청정기의 위치 찾아줌
    cleaner = []
    for i in range(R):
        if A[i][0] == -1:
            cleaner.append((i, 0))

    # 시계 반대방향(우상좌하)로 dy, dx 지정
    top_dy = [0, -1, 0, 1]
    top_dx = [1, 0, -1, 0]
    # dy와 dx의 인덱스 0으로 초기화
    top_idx = 0
    # cleaner가 위쪽행부터 탐색했으므로 cleaner의 맨 앞 값을 위쪽의 시작점으로 지정
    tsy, tsx = cleaner[0]
    # 큐에는 어떤 지점의 (y좌표, x좌표, 미세먼지 양) 넣기
    tq = deque()
    tq.append((tsy, tsx, 0))

    while True:
        # y좌표, x 좌표, 미세먼지양 pop해서 변수에 저장
        y, x, amount = tq.popleft()

        # dy, dx, idx로 다음 탐색 지점 설정
        ny = y + top_dy[top_idx]
        nx = x + top_dx[top_idx]

        # 다음 탐색 지점이 범위 밖이라면 idx 바꿔줘야 함
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            # 현재 idx가 3이면 0으로, 나머지는 1 증가
            if top_idx == 3:
                top_idx = 0
            else:
                top_idx += 1
            # 다음 탐색 지점 다시 설정
            ny = y + top_dy[top_idx]
            nx = x + top_dx[top_idx]

        # 만약 다음 탐색 지점이 공기청정기 위치라면 break
        # 원래 pop하고 확인하려 했으나 시작점에서 걸려서 다음 탐색 지점 설정 후 확인함
        if ny == tsy and nx == tsx:
            break

        # 큐에 다음 탐색 지점의 (y좌표, x좌표, 미세먼지 양) 넣기
        tq.append((ny, nx, A[ny][nx]))
        # 다음 탐색 지점의 값을 이전 위치의 미세먼지 양으로 업데이트
        A[ny][nx] = amount

    # top과 로직은 동일, 방향만 다름
    bottom_dy = [0, 1, 0, -1]
    bottom_dx = [1, 0, -1, 0]
    bottom_idx = 0
    bsy, bsx = cleaner[1]
    bq = deque()
    bq.append((bsy, bsx, 0))

    while True:
        y, x, amount = bq.popleft()

        ny = y + bottom_dy[bottom_idx]
        nx = x + bottom_dx[bottom_idx]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            if bottom_idx == 3:
                bottom_idx = 0
            else:
                bottom_idx += 1
            ny = y + bottom_dy[bottom_idx]
            nx = x + bottom_dx[bottom_idx]

        if ny == bsy and nx == bsx:
            break

        bq.append((ny, nx, A[ny][nx]))
        A[ny][nx] = amount


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 확산과 공기청정기 작동이 T번 반복
for _ in range(T):
    spread()
    air_cleaner()

print(sum(sum(A, [])) + 2)