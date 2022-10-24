# 방향 : 우, 좌, 상, 하
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def game():
    turn = 0

    while True:
        # 턴수 증가, 1000 넘었다면 -1 리턴
        turn += 1
        if turn > 1000:
            return -1

        # 1번말부터 차례대로 위치와 방향 -> 다음 방향 설정
        for num in range(1, K + 1):
            hy, hx, hd = horse[num]
            ny = hy + dy[hd]
            nx = hx + dx[hd]

            # 다음 방향이 파란색 또는 범위 벗어나는 경우
            if not(0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                # 방향 바꾸기
                if hd in [0, 2]:
                    hd += 1
                elif hd in [1, 3]:
                    hd -= 1

                # 말의 정보에서 방향 바꿔주고, 바꾼 방향으로 이동
                horse[num][2] = hd
                ny = hy + dy[hd]
                nx = hx + dx[hd]

                # 한번 더 다음 방향이 파란색 또는 범위 벗어나는 경우 가만히 있기
                if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                    continue

            # 다음 방향이 흰색 판이라면
            if board[ny][nx] == 0:
                # 현재 말이 있는 위치의 말탑 중에 몇번째인지 위치 찾기
                pos = horse_on_board[hy][hx].index(num)

                # 말탑에서 위치~꼭대기까지 말의 번호 알아와서 다음 위치로 옮기기
                for p in range(pos, len(horse_on_board[hy][hx])):
                    n = horse_on_board[hy][hx][p]
                    horse[n][0] = ny
                    horse[n][1] = nx

                # 판에 있는 말 정보 바꾸기 -> 이전 위치는 슬라이싱으로 윗부분 잘라내고, 이후 위치는 기존 말 + 슬라이싱으로 잘라낸 윗부분
                horse_on_board[ny][nx].extend(horse_on_board[hy][hx][pos:])
                horse_on_board[hy][hx] = horse_on_board[hy][hx][:pos]

                # 이동시켰을 때 길이가 4가 넘으면 턴수 리턴
                if len(horse_on_board[ny][nx]) >= 4:
                    return turn

            # 흰색 판과 동일, 슬라이싱으로 잘라낸 윗부분을 이동 위치로 옮길 때 역순으로 옮기는거 빼고 동일
            elif board[ny][nx] == 1:
                pos = horse_on_board[hy][hx].index(num)

                for p in range(pos, len(horse_on_board[hy][hx])):
                    n = horse_on_board[hy][hx][p]
                    horse[n][0] = ny
                    horse[n][1] = nx

                horse_on_board[ny][nx].extend(reversed(horse_on_board[hy][hx][pos:]))
                horse_on_board[hy][hx] = horse_on_board[hy][hx][:pos]

                if len(horse_on_board[ny][nx]) >= 4:
                    return turn


N, K = map(int, input().split())
# board는 판의 정보
# horse는 말의 정보 -> 딕셔너리 키 : 말의 번호, 값 : (y 위치, x 위치, 이동 방향)
# horse_on_board는 판에 있는 말의 상태
board = [list(map(int, input().split())) for _ in range(N)]
horse = dict()
horse_on_board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(0, K):
    y, x, d = map(int, input().split())
    horse[i + 1] = [y - 1, x - 1, d - 1]
    horse_on_board[y - 1][x - 1].append(i + 1)

print(game())