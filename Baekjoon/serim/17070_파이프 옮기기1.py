n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i - 1][j] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))