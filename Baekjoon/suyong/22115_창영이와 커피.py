N, K = map(int, input().split())
coffee = list(map(int, input().split()))
cant = float('inf')
dp = [[cant] * (N + 1) for _ in range(K + 1)]
dp[0] = [0] * (N + 1)
# dp 행을 카페인, 열을 커피 인덱스로 설정
for i in range(1, K + 1):
    for j in range(1, N + 1):
        # 현재 카페인 - 커피 카페인 < 0 인 경우 -> 불가능한 경우
        if i - coffee[j - 1] < 0:
            dp[i][j] = dp[i][j - 1]
        # 현재 커피 dp계산 전과 현재 커피 마시기 전, 두 경우가 모두 불가능하면 계산 불가능
        elif dp[i - coffee[j - 1]][j - 1] != cant or dp[i][j - 1] != cant:
            #현재 커피 dp계산 전 vs 현재 커피 처리 후(dp[현재 커피 마시기 전 카페인][현재커피 처리 전까지 마신 커피 개수] + 1)
            dp[i][j] = min(dp[i][j - 1], dp[i - coffee[j - 1]][j - 1] + 1)
if dp[K][N] == cant:
    print(-1)
else:
    print(dp[K][N])