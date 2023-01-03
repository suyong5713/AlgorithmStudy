from collections import deque

# 방향
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
arr = []


# 직사각형 그리기 함수
def draw_rectangle(point):
    # 좌측 하단의 좌표와 우측 상단의 좌표 받아옴
    sx, sy, ex, ey = point
    # 직사각형 세로
    for y in range(sy, ey + 1):
        # 직사각형 가로
        for x in range(sx, ex + 1):
            # 좌측 하단의 좌표나 우측 상단의 좌표와 같다면
            # 해당 직사각형의 테두리임!
            # 0: 빈칸, 1: 직사각형 테두리, 2: 직사각형 내부
            if x == sx or x == ex or y == sy or y == ey:
                # 해당 칸이 빈 칸인 경우에만 테두리로 색칠
                # 빈 칸이 아니라면 이미 다른 직사각형이 존재하기에 해줄 필요 없음
                if arr[y][x] == 0:
                    arr[y][x] = 1
            # 아니라면 직사각형의 내부이므로 2를 대입
            else:
                arr[y][x] = 2


# 칸이 붙어있을 때 정확한 테두리로 인식하기 어려운 문제가 발생했음
# 따라서 기존 필요한 칸보다 2배 늘리고 좌표도 2배 늘렸음.
# 이후에 BFS 결과로 나오는 distance는 반대로 2로 나누어줬음.
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    # 가로와 세로의 최대값을 구함
    xmax = max([max(rec[0], rec[2]) for rec in rectangle])
    ymax = max([max(rec[1], rec[3]) for rec in rectangle])

    # 가로와 세로의 최대 크기에 대한 2차원 배열 생성
    for _ in range((ymax + 1) * 2):
        arr.append([0] * ((xmax + 1) * 2))

    # 입력받은 직사각형 그려줌
    for rec in rectangle:
        draw_rectangle(tuple([int(r) * 2 for r in rec]))

    # 방문 확인용 배열 생성
    visited = [[-1] * ((xmax + 1) * 2) for _ in range((ymax + 1) * 2)]

    # 큐 생성
    q = deque()
    visited[characterY * 2][characterX * 2] = 0
    q.append((characterX * 2, characterY * 2))

    while q:
        x, y = q.popleft()
        # 해당 지점이 아이템 좌표라면
        # 해당 좌표의 visited를 2로 나눈 값을 결과로 가져오고 반복 종료
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[y][x] // 2
            break
        # 4방향 탐색
        for dx, dy in dir:
            px, py = x + dx, y + dy
            # 정해진 칸 범위 내에 없을 시 탐색하지 않음
            if not (0 <= px < (xmax + 1) * 2 and 0 <= py < (ymax + 1) * 2): continue
            # 해당 지점을 방문하지 않았으며 테두리일 경우
            if visited[py][px] == -1 and arr[py][px] == 1:
                # 해당 지점을 방문처리(기존 distance+1)한 후
                # 큐에 해당 좌표 삽입
                visited[py][px] = visited[y][x] + 1
                q.append((px, py))

    return answer