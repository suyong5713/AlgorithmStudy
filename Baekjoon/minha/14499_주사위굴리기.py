def dice_move(direction):
    # 1 -> 동쪽으로 굴렸을 때 전개도 변화하는 함수
    if direction == 1:
        dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
        end = dice[1][2]
        for i in range(2, 0, -1):
            dice[1][i] = dice[1][i - 1]
        dice[1][0] = end
    # 2 -> 서쪽으로 굴렸을 때 전개도 변화하는 함수
    elif direction == 2:
        dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
        end = dice[1][0]
        for i in range(0, 2):
            dice[1][i] = dice[1][i + 1]
        dice[1][2] = end
    # 3 -> 북쪽으로 굴렸을 때 전개도 변화하는 함수
    elif direction == 3:
        end = dice[0][1]
        for i in range(0, 3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = end
    # 4 -> 남쪽으로 굴렸을 때 전개도 변화하는 함수
    else:
        end = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = end

N, M, y, x, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

# 주사위 초기 전개도
dice = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 1 -> 동, 2 -> 서, 3 -> 북, 4 -> 남쪽 방향이 되도록 설정
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

# 명령 하나씩 반복문 돌면서
for o in order:
    # 주사위가 놓일 좌표 변경
    y += dy[o]
    x += dx[o]

    # 주사위가 놓일 좌표가 범위를 벗어나면 원래 값으로 복구시키고 다음 반복문 돌게 함
    if not(0 <= y < N and 0 <= x < M):
        y -= dy[o]
        x -= dx[o]
        continue

    # 주사위 굴리기 -> 23288번 문제 동서남북 함수 재사용..
    dice_move(o)
    # 주사위가 놓인 칸의 값과 주사위 바닥의 숫자
    graph_num = graph[y][x]
    dice_floor_num = dice[3][1]

    # 주사위 윗면 출력
    print(dice[1][1])

    # 주사위가 놓인 칸이 0이면 그 칸에 주사위의 바닥면 숫자 복사
    if graph_num == 0:
        graph[y][x] = dice_floor_num
    # 주사위가 놓인 칸이 0이 아니면
    # 주사위의 바닥면 숫자에 그 칸의 숫자 복사
    # 그 칸은 0이 됨
    else:
        dice[3][1], graph[y][x] = graph_num, 0