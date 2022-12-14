N = int(input())

time = []
cost = []
dp = [0] * (N + 1)

for _ in range(N):
    T, P = map(int, input().split())
    time.append(T)
    cost.append(P)

for i in range(N - 1, -1, -1):
    # i일+i일 완료하는데 걸리는 시간(즉, 상담이 끝나는 날)이 N일보다 크다면 dp[i]=dp[i+1]
    if time[i] + i > N:
        dp[i] = dp[i + 1]
    # 그 외에는 두 가지 경우를 비교해 큰 값을 해당일의 최댓값으로 구한다
    # 1) i일의 일을 하는 경우 -> i일의 cost+i일의 상담이 끝나는 날의 dp값 -> cost[i] + dp[i+time[i]]
    # 2) i일의 일을 하지 않는 경우 -> dp[i]=dp[i+1]
    else:
        dp[i] = max(cost[i] + dp[i + time[i]], dp[i + 1])

print(dp[0])