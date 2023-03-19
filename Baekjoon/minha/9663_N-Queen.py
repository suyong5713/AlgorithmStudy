# 퀸은 자신을 기준으로 일직선상(가로 및 세로)과 대각선 방향에는 아무것도 놓여 있으면 안됨
def is_possible(row):
    for chk in range(row):
        if rows[row] == rows[chk] or abs(rows[row] - rows[chk]) == abs(row - chk):
            return False
    return True

def n_queens(row):
    global answer

    if row == N:
        answer += 1
    else:
        for col in range(N):
            rows[row] = col
            if is_possible(row):
                n_queens(row + 1)

N = int(input())

rows = [0] * N
answer = 0
n_queens(0)
print(answer)