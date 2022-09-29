from collections import deque

def make_order(y, x):
    # 칸의 순서 구하기위한 방향, 순서대로 좌하우상
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    # 이동 거리
    length = 0

    # 좌상단 갈때까지 4방향 반복하면서
    while True:
        for i in range(4):
            # 방향이 왼쪽이나 오른쪽인 경우 이동 거리 증가
            if i % 2 == 0:
                length += 1
            # 이동거리만큼 한칸씩 이동하며 order에 좌표 저장
            for j in range(length):
                y += dy[i]
                x += dx[i]
                order.append((y, x))
                # 좌상단에 도착한 경우 종료
                if x == 0 and y == 0:
                    return

def blizard(direction, space, y, x):
    # 문제에서 주어진 4가지 방향, 순서대로 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 마볍 방향쪽으로 이동 거리만큼 반복하며 0으로 값 변경
    for _ in range(space):
        y += dy[direction]
        x += dx[direction]
        graph[y][x] = 0

def move():
    # 빈칸을 담을 큐
    blank = deque()
    # 순서대로 돌면서
    for y, x in order:
        # 빈칸인 경우 큐에 좌표 넣기
        if graph[y][x] == 0:
            blank.append((y, x))
        # 현재 칸이 빈칸이 아닌데 앞에 다른 빈칸이 존재하는 경우
        elif graph[y][x] > 0 and blank:
            # 빈칸 큐에서 가장 앞의 좌표 가져와서 그 곳에 현재칸의 값을 넣어주고, 현재칸은 빈칸으로 만들고 큐에 넣는다
            ny, nx = blank.popleft()
            graph[ny][nx] = graph[y][x]
            graph[y][x] = 0
            blank.append((y, x))

def boom():
    global one, two, three

    # bomb 없이 같은 값이면 바로 0으로 바꿔주려고 했으나, cnt가 4보다 작은 경우 때문에 안됨..
    bomb = []
    cnt = 0
    number = -1
    flag = False

    # 순서대로 돌면서
    for y, x in order:
        # 맨 처음 좌표일 때
        if number == -1:
            # number 설정, cnt 증가하고 좌표값 bomb에 넣기
            number = graph[y][x]
            cnt += 1
            bomb.append((y, x))
        # 맨 처음 좌표가 아닌 경우
        else:
            # 현재 number와 좌표의 값이 같은 경우 cnt 증가하고 좌표값 bomb에 넣기
            if number == graph[y][x]:
                cnt += 1
                bomb.append((y, x))
            # 현재 number와 좌표의 값이 다른 경우
            else:
                # cnt가 4보다 크면 -> 폭발
                # flag 설정, 구슬 카운트 증가, bomb 리스트의 좌표값 0으로 바꿔주기
                if cnt >= 4:
                    flag = True
                    if number == 1:
                        one += cnt
                    elif number == 2:
                        two += cnt
                    else:
                        three += cnt

                    for by, bx in bomb:
                        graph[by][bx] = 0

                # cnt가 4보다 큰 경우와 아닌 경우 모두
                # number 설정, cnt과 bomb 재설정
                number = graph[y][x]
                cnt = 1
                bomb = [(y, x)]

    # 폭발이 됐는지 확인하기 위해 flag 리턴
    return flag

def change():
    number = -1
    cnt = 0
    marble = deque()

    # 순서대로 돌면서
    for y, x in order:
        # 맨 처음 좌표일 때
        if number == -1:
            # number 설정, cnt 증가
            number = graph[y][x]
            cnt += 1
        # 맨 처음 좌표가 아닌 경우
        else:
            # 현재 number와 좌표의 값이 같은 경우 cnt 증가
            if number == graph[y][x]:
                cnt += 1
            # 현재 number와 좌표의 값이 다른 경우 이전 구슬 그룹의 갯수와 숫자 큐에 넣어주고 number와 cnt 새로운 값으로 갱신
            else:
                marble.append(cnt)
                marble.append(number)
                number = graph[y][x]
                cnt = 1

    # 순서대로 돌면서 marble 큐에 값이 존재하면 해당 좌표에 큐의 맨 앞 원소값 대입, 큐에 값이 없으면 0 대입
    for y, x in order:
        if marble:
            graph[y][x] = marble.popleft()
        else:
            graph[y][x] = 0

# 입력 받기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]

# 구슬 갯수와 가운데 위치
one, two, three = 0, 0, 0
center_y, center_x = N // 2, N // 2

# 칸의 순서 좌표값으로 저장하기
order = []
make_order(center_y, center_x)

# 마법 횟수만큼 반복
for d, s in magic:
    # 블리자드 마법 -> 방향, 거리와 중앙값 인자로
    blizard(d - 1, s, center_y, center_x)
    # 마법 후 이동
    move()

    # 폭발하는 구슬이 없을 때까지 폭발 -> 이동 반복
    while True:
        flag = boom()
        if not flag:
            break
        move()

    # 변화
    change()

print(one + 2 * two + 3 * three)