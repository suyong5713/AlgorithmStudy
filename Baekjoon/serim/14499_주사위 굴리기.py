def change_num(command):
    global dice
    if command == 1: # 동
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif command == 2:  # 서
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif command == 3:  # 북
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif command == 4:  # 남
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


dice = [0, 0, 0, 0, 0, 0]   # 아랫면은 6번, 윗면은 1번
# 0, 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
# 세로 크기, 가로 크기, 좌표, 명령 개수
n, m, x, y, k = map(int, input().split())
# 지도 위 숫자
nums = [list(map(int, input().split())) for _ in range(n)]
# 명령
commands = list(map(int, input().split()))

for command in commands:
    nx = x + dx[command]
    ny = y + dy[command]
    # 지도 위로 이동한 경우에만 실행
    if 0 <= nx < n and 0 <= ny < m:
        change_num(command)
        # 지도 위 숫자가 0일 경우
        if nums[nx][ny] == 0:
            nums[nx][ny] = dice[5]
        # 지도 위 숫자가 0이 아닐 경우
        else:
            dice[5] = nums[nx][ny]
            nums[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])