from copy import deepcopy

def move():
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                m, s, d = board[i][j][k]
                ny = (i + s * dy[d]) % N
                nx = (j + s * dx[d]) % N
                update_board[ny][nx].append((m, s, d))


def join_and_divide():
    for i in range(N):
        for j in range(N):
            cnt = len(update_board[i][j])
            if cnt >= 2:
                sum_m, sum_s, cnt_odd, cnt_even = 0, 0, 0, 0
                for k in range(cnt):
                    sum_m += update_board[i][j][k][0]
                    sum_s += update_board[i][j][k][1]
                    if update_board[i][j][k][2] % 2 == 1:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                nm = int(sum_m / 5)
                ns = int(sum_s / cnt)
                update_board[i][j] = []
                if nm != 0:
                    if cnt_odd == cnt or cnt_even == cnt:
                        for d in range(4):
                            update_board[i][j].append((nm, ns, d * 2))
                    else:
                        for d in range(4):
                            update_board[i][j].append((nm, ns, d * 2 + 1))


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fire_ball = [list(map(int, input().split())) for _ in range(M)]

board = [[[] for _ in range(N)] for _ in range(N)]
# 위치 r, 위치 c - (r행 c열), 질량 m, 속력 s, 방향 d
for r, c, m, s, d in fire_ball:
    board[r - 1][c - 1].append((m, s, d))

for _ in range(K):
    update_board = [[[] for _ in range(N)] for _ in range(N)]
    move()
    join_and_divide()
    board = deepcopy(update_board)

answer = 0
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]

print(answer)