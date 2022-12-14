import sys
sys.stdin = open("input.txt", "r")

n = int(input())
# t, p
tp = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]
# 마지막 날부터 계산
for i in range(n - 1, -1, -1):
    # 상담이 끝나는 날이 n보다 크면 할 수 없음
    if i + tp[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # 상담을 하지 않을 경우 vs 상담을 할 경우
        dp[i] = max(dp[i + 1], tp[i][1] + dp[i + tp[i][0]])
print(dp[0])
