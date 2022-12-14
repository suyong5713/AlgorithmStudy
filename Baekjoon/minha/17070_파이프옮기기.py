N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for i in range(N)] for i in range(N)] for i in range(3)]
dp[0][0][1] = 1

# 첫줄은 가로
for i in range(2, N):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

# 두번째 줄부터
for i in range(1, N):
    for j in range(2, N):
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

        if board[i][j] == 0:
            # 가로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(sum(dp[d][N-1][N-1] for d in range(3)))