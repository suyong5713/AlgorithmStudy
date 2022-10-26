dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, K = map(int, input().split())

# https://velog.velcdn.com/images/alsgk721/post/c1060408-922b-4272-a08f-fe7574e327e8/image.jpeg
graph = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
priority = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

# 좌표별 [상어 번호, 냄새 지속 시간]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

time = 0

while True:
    for smy in range(N):
        for smx in range(N):
            # 좌표별로 탐색하며 냄새 지속시간이 0보다 큰 경우 1씩 감소
            if smell[smy][smx][1] > 0:
                smell[smy][smx][1] -= 1
            # 좌표별로 탐색하며 상어가 존재한다면 해당 칸에 냄새 정보
            if graph[smy][smx] != 0:
                smell[smy][smx] = [graph[smy][smx], K]

    # 이동 정보를 담을 리스트
    next_graph = [[0] * N for _ in range(N)]

    # 칸별로 상어가 이동
    for cy in range(N):
        for cx in range(N):
            # 그래프의 값이 상어의 번호
            shark_num = graph[cy][cx]
            # 해당 칸에 상어가 존재하면 냄새가 없는 칸 탐색
            if shark_num > 0:
                # 상어의 방향 : direction[상어의 번호 - 1]
                cur_dir = direction[shark_num - 1]
                flag1 = False
                for d in range(4):
                    # 다음 방향 priority 리스트에서 확인 -> 상어의 번호, 현재 방향에서의 우선순위에 따라 다음 방향 탐색
                    next_dir = priority[shark_num - 1][cur_dir - 1][d]
                    ny = cy + dy[next_dir - 1]
                    nx = cx + dx[next_dir - 1]
                    if 0 <= ny < N and 0 <= nx < N:
                        # 다음 방향이 범위 내에 있고, 비어 있다면 방향 바꾸기
                        if smell[ny][nx][1] == 0:
                            direction[shark_num - 1] = next_dir

                            # 이동할 칸이 비었다면 옮기기, 비어 있지 않다면 현재 있는 값과 비교해서 작은 값으로
                            if next_graph[ny][nx] == 0:
                                next_graph[ny][nx] = graph[cy][cx]
                            else:
                                next_graph[ny][nx] = min(next_graph[ny][nx], graph[cy][cx])

                            flag1 = True
                            break

                # 첫번째 조건(냄새가 없는 칸)에서 이동할 칸을 찾았다면 다음 칸 탐색
                if flag1:
                    continue

                # 사방의 칸이 모두 냄새가 있는 칸이면 자신의 냄새 탐색
                for d in range(4):
                    next_dir = priority[shark_num - 1][cur_dir - 1][d]
                    ny = cy + dy[next_dir - 1]
                    nx = cx + dx[next_dir - 1]
                    if 0 <= ny < N and 0 <= nx < N:
                        # 이동할 칸의 냄새가 자신의 냄새이면 옮기기
                        if smell[ny][nx][0] == graph[cy][cx]:
                            direction[shark_num - 1] = next_dir
                            next_graph[ny][nx] = graph[cy][cx]
                            break

    graph = next_graph
    time += 1

    # 1번 상어 외에 다른 상어가 있는지 확인
    flag2 = True
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 1:
                flag2 = False

    # 1번 상어만 남았다면
    if flag2:
        print(time)
        break

    # 1000초가 넘었다면 -1 출력
    if time >= 1000:
        print(-1)
        break