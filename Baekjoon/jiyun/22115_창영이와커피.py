MAX = 1e9  # float('inf') -> 1e9는 유한한 수이기에, 비교 연산시 더 편함. -> elif not dp[i-arr[j-1]][j-1]== MAX and dp[i][j-1]== MAX: 가 필요 없어짐.

def solution():
    for i in range(1, k+1):             # 행 (=카페인)
        for j in range(1, n+1):         # 열 (=커피)
            now = arr[j-1]
            if i< now:                  # 불가능 한 경우 (= 카페인 초과할 경우)
                dp[i][j]=dp[i][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - arr[j - 1]][j - 1] + 1)
    return -1 if dp[k][n]==MAX else dp[k][n]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1)] + [[MAX] * (n + 1) for _ in range(k)]
print(solution())
