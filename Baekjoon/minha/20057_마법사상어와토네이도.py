def move(dis, dy, dx, per):
    global answer, x, y

    # 특정 방향으로 dis만큼 반복하며 토네이도 지나갔을 때 모래값 등 정보 갱신
    for _ in range(dis):
        # 토네이도가 이동할 좌표 지정, 해당 좌표에 있는 모래값 target_sand에 저장
        ny, nx = y + dy, x + dx
        target_sand = sand[ny][nx]

        # 비율이 적혀있는 칸으로 이동한 모래의 양을 구할 spread와 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양을 더할 좌표 초기화
        spread = 0
        remain_y, remain_x = 0, 0

        for i in range(5):
            for j in range(5):
                # 비율을 저장한 배열을 돌면서 -1(남은 모래양 더할 곳)이면 해당 좌표를 remain_y와 remain_x 지정
                if per[i][j] == -1:
                    remain_y = ny + (i - 2)
                    remain_x = nx + (j - 2)
                # 0보다 크면(모래가 이동할 좌표) 모래가 이동할 좌표인 (my, mx)와 해당 좌표에 이동할 모래의 양 ms를 구함
                if per[i][j] > 0:
                    my = ny + (i - 2)
                    mx = nx + (j - 2)
                    ms = int(target_sand * per[i][j] / 100)
                    # (my, mx)가 좌표 범위 내에 있으면 spread에 해당 값을 더해주고, sand에도 그 양만큼 더해줌
                    if 0 <= my < N and 0 <= mx < N:
                        spread += ms
                        sand[my][mx] += ms
                    # 범위 밖에 있으면 spread에 해당 값을 더해주고, answer에도 그 양만큼 더해줌
                    else:
                        spread += ms
                        answer += ms

        # 남은 모래양을 더할 좌표가 범위 내에 있으면 그 좌표에 그 모래양만큼 더해줌
        if 0 <= remain_y < N and 0 <= remain_x < N:
            sand[remain_y][remain_x] += (target_sand - spread)
        # 범위 밖에 있으면 answer에 남은 모래양만큼을 더해줌
        else:
            answer += (target_sand - spread)

        # 해당 좌표에는 이제 모래가 없으므로 0으로 값을 변경해주고, y와 x값도 ny와 nx로 갱신해줌
        sand[ny][nx] = 0
        y, x = ny, nx


# 비율은 하드코딩 했습니다..
left = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, -1, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
right = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, -1, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
up = [[0, 0, 5, 0, 0], [0, 10, -1, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
down = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, -1, 10, 0], [0, 0, 5, 0, 0]]

N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
# 토네이도 시작 좌표(y, x)
y, x = N // 2, N // 2
# 범위 밖으로 나간 모래의 양을 더할 answer
answer = 0

# i+1이 홀수 -> 홀수 길이만큼 움직일 때 : 왼쪽, 아래쪽
# i+1이 짝수 -> 짝수 길이만큼 움직일 때 : 오른쪽, 위
# 마지막 왼쪽으로 갈 때는 i+1이 아닌 i만큼 왼쪽으로만 움직여서 따로 조건문 작성
for i in range(N):
    if i == N - 1:
        move(i, 0, -1, left)
    else:
        if i % 2 == 0:
            move(i + 1, 0, -1, left)
            move(i + 1, 1, 0, down)
        else:
            move(i + 1, 0, 1, right)
            move(i + 1, -1, 0, up)

print(answer)