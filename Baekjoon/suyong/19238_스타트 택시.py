def BFS(row, col, visited):
    global matrix
    queue = [[row, col]]
    visited[row][col] = 1
    while queue:
        row, col = queue.pop(0)
        for d_row, d_col in [-1, 0], [0, -1], [1, 0], [0, 1]:
            n_row, n_col = row + d_row, col + d_col
            if 0 <= n_row < N and 0 <= n_col < N:
                if not visited[n_row][n_col] and matrix[n_row][n_col] != 1:
                    queue.append([n_row, n_col])
                    visited[n_row][n_col] += visited[row][col] + 1
    return

N, M, fuel = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
taxi_pos = list(map(int, input().split()))
start_end = [list(map(int, input().split())) for _ in range(M)]

# 행, 열 번호 인덱스화
taxi_pos = [taxi_pos[0] - 1, taxi_pos[1] - 1]
for i in range(M):
    for j in range(4):
        start_end[i][j] -= 1

while True:
    # 연료 다 떨어지면 실패
    if fuel < 0:
        fuel = -1
        break
    # 더이상 손님이 없으면 종료
    if not start_end:
        break
    visited = [[0] * N for _ in range(N)]
    row, col = taxi_pos
    BFS(row, col, visited)
    passenger_list = []
    for passenger in start_end:
        s_row, s_col, e_row, e_col = passenger
        # 거리잴 때 1부터 시작했으니 -1
        distance = visited[s_row][s_col] - 1
        passenger_list.append([distance, s_row, s_col, e_row, e_col])
    # 거리, 행, 열에 대해 오름차순
    passenger_list.sort(key=lambda x: (x[0], x[1], x[2]))
    # 최단거리 승객 탑승
    passenger = passenger_list[0]
    # 승객과의 거리가 -1인경우 -> BFS탐색 불가능한 경우
    if passenger[0] < 0:
        # 승객 태우러 못감
        fuel = -1
        break
    # 승객을 태웠으니 리스트에서 제거
    if start_end:
        start_end.remove(passenger[1:])
        # 승객과의 거리만큼 연료 소비
        fuel -= (visited[passenger[1]][passenger[2]] - 1)
    visited = [[0] * N for _ in range(N)]
    # 승객 -> 도착지 거리계산
    BFS(passenger[1], passenger[2], visited)
    # 거리만큼 연료 소모
    fuel -= (visited[passenger[3]][passenger[4]] - 1)

    # 이동 성공
    if fuel >= 0:
        # 연료 충전
        fuel += (visited[passenger[3]][passenger[4]] - 1) * 2
        # 택시위치 변경
        taxi_pos = [passenger[3], passenger[4]]
    # 이동 실패
    else:
        fuel = -1
        break
print(fuel)