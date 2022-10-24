dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def game():
    turn = 0

    while True:
        turn += 1
        if turn > 1000:
            return -1

        for num in range(1, K + 1):
            hy, hx, hd = horse[num]
            ny = hy + dy[hd]
            nx = hx + dx[hd]

            # 파란색 또는 범위 벗어나는 경우
            if not(0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                if hd in [0, 2]:
                    hd += 1
                elif hd in [1, 3]:
                    hd -= 1

                ny = hy + dy[hd]
                nx = hx + dx[hd]
                horse[num][2] = hd

                if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                    continue

            if board[ny][nx] == 0:
                pos = horse_on_board[hy][hx].index(num)

                for p in range(pos, len(horse_on_board[hy][hx])):
                    n = horse_on_board[hy][hx][p]
                    horse[n][0] = ny
                    horse[n][1] = nx

                horse_on_board[ny][nx].extend(horse_on_board[hy][hx][pos:])
                horse_on_board[hy][hx] = horse_on_board[hy][hx][:pos]

                if len(horse_on_board[ny][nx]) >= 4:
                    return turn

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
board = [list(map(int, input().split())) for _ in range(N)]
horse = dict()
horse_on_board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(0, K):
    y, x, d = map(int, input().split())
    horse[i + 1] = [y - 1, x - 1, d - 1]
    horse_on_board[y - 1][x - 1].append(i + 1)

print(game())