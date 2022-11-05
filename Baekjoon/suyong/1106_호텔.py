C, N = map(int,input().split())
cost_and_people = [list(map(int,input().split())) for _ in range(N)]
max_people = sorted(cost_and_people, key = lambda x: x[1])[-1][1]
dp = [float("inf")] * (C + max_people)
dp[0] = 0
#점화식 세우기!
#dp[유치 후 인원] = min(dp[유치 전 인원] + 비용, dp[유치 후 인원])
#예를들어 dp[3 + 2] = min(dp[3 + 2 - 2] + cost, dp[3 + 2])
#기존의 5명을 만드는 비용과, 현재 방법으로 5명을 만드는 비용을 비교해서 더 작은것을 채택.
for cost, people in cost_and_people:
  for i in range(people, len(dp)):
    dp[i] = min(dp[i - people] + cost, dp[i])
#최소 N명을 만들어야 함
print(min(dp[C:]))