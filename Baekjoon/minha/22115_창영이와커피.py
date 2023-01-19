N, K = map(int, input().split())
C = list(map(int, input().split()))

# 행 : 카페인의 양 + 1인 표, 열 : 커피 종류의 개수 + 1
dp = [[0] * (N + 1)] + [[1e9] * (N + 1) for _ in range(K)]

for caffeine in range(1, K + 1):  # 행
    for coffee in range(1, N + 1):  # 열
        cur_caf = C[coffee - 1] # 현재 커피의 카페인

        if caffeine < cur_caf:  # 현재 커피의 카페인이 체크하는 카페인보다 클 때
            dp[caffeine][coffee] = dp[caffeine][coffee-1]
        else:
            # 더 나은 경우를 찾는다.
            dp[caffeine][coffee] = min(dp[caffeine][coffee - 1], dp[caffeine - cur_caf][coffee - 1] + 1)

if dp[K][N] == 1e9:
    print(-1)
else:
    print(dp[K][N])