def find_seat(num, like):
    # num번 학생의 자리를 찾기 위해 먼저 모든 좌석에 대해 탐색 수행
    # (i, j)가 빈 자리라면 인접한 자리들을 탐색하며 인접한 자리에 있는 학생이 좋아하는 학생 리스트에 존재하면 카운트 증가
    # adj는 학생이 (i, j)자리에 존재한다면 인접하는 자리에 좋아하는 학생이 몇명 있는지를 저장
    adj = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt = 0
                for k in range(4):
                    adj_y, adj_x = i + dy[k], j + dx[k]
                    if 0 <= adj_y < N and 0 <= adj_x < N and visited[adj_y][adj_x]:
                        if seat[adj_y][adj_x] in like:
                            cnt += 1
                adj[i][j] = cnt

    # adj 리스트에서 최댓값을 찾고, adj 리스트를 탐색하며 그 최댓값에 해당하고, 비어 있는 자리라면 possible 리스트에 그 자리의 좌표 넣기
    max_cnt = max(sum(adj, []))
    possible = []
    for i in range(N):
        for j in range(N):
            if adj[i][j] == max_cnt and not visited[i][j]:
                possible.append((i, j))

    # possible 리스트에 원소가 하나라면 -> 그 자리에 방문 처리하고, 그 학생의 자리로 지정후 함수 리턴
    if len(possible) == 1:
        y, x = possible.pop()
        visited[y][x] = True
        seat[y][x] = num
        return
    # possible 리스트에 원소가 하나가 아니면 -> 2번 조건 실행
    else:
        # possible 리스트의 원소를 탐색하며 인접한 자리가 비어 있는 자리라면 카운트 증가
        # empty는 (i, j)의 인접한 자리 중 비어 있는 자리의 갯수를 저장
        empty = [[-1] * N for _ in range(N)]
        for py, px in possible:
            cnt = 0
            for i in range(4):
                adj_y, adj_x = py + dy[i], px + dx[i]
                if 0 <= adj_y < N and 0 <= adj_x < N:
                    if not visited[adj_y][adj_x]:
                        cnt += 1

            empty[py][px] = cnt

        # empty 리스트에서 최댓값을 찾고, empty 리스트를 탐색하며 그 최댓값에 해당하고, 비어 있는 자리라면 possible2 리스트에 그 자리의 좌표 넣기
        max_cnt2 = max(sum(empty, []))
        possible2 = []
        for i in range(N):
            for j in range(N):
                if empty[i][j] == max_cnt2 and not visited[i][j]:
                    possible2.append((i, j))

        # possible2 리스트에 원소가 하나라면 -> 그 자리에 방문 처리하고, 그 학생의 자리로 지정후 함수 리턴
        if len(possible2) == 1:
            y, x = possible2.pop()
            visited[y][x] = True
            seat[y][x] = num
            return
        # possible2 리스트에 원소가 하나가 아니면 -> 3번 조건 실행
        else:
            # possible2를 행 기준->열 기준으로 정렬 후 possible2를 탐색하며 비어있는 자리라면 방문 처리하고, 그 학생의 자리로 지정후 함수 리턴
            possible2.sort(key=lambda x: (x[0], x[1]))
            for y, x in possible2:
                if not visited[y][x]:
                    visited[y][x] = True
                    seat[y][x] = num
                    return


def calculate_score():
    global answer

    # 모든 좌석을 탐색하며 인접한 자리에 좋아하는 학생 수 카운트 후 점수 계산
    for i in range(N):
        for j in range(N):
            num = seat[i][j]
            cnt = 0
            for k in range(4):
                adj_y, adj_x = i + dy[k], j + dx[k]
                if 0 <= adj_y < N and 0 <= adj_x < N:
                    if seat[adj_y][adj_x] in likes[num]:
                        cnt += 1
            if cnt > 0:
                answer += 10**(cnt - 1)


# 입력 받기
N = int(input())
students = [list(map(int, input().split())) for _ in range(N * N)]

# order는 자리 배정하는 학생의 순서
# likes는 이차원 배열로 i번째 리스트는 i번 학생이 좋아하는 학생의 번호 리스트
order = []
likes = [[] for _ in range(N * N + 1)]
for s in students:
    order.append(s[0])
    likes[s[0]] = s[1:]

# 자리가 차지되었음을 표시하는 visited
# 자리에 몇번 학생이 있는지를 표시하는 seat
visited = [[False] * N for _ in range(N)]
seat = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 학생의 순서대로 자리를 찾게 함
for o in order:
    find_seat(o, likes[o])

# 자리를 찾았으면 만족도 계산
answer = 0
calculate_score()

print(answer)