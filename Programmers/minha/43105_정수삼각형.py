def solution(triangle):
    for r in range(len(triangle)):
        triangle[r] = [0] + triangle[r] + [0]

    dp = [[0] * len(triangle[r]) for r in range(len(triangle))]
    dp[0][1] = triangle[0][1]

    for r in range(1, len(triangle)):
        for c in range(1, len(triangle[r]) - 1):
            dp[r][c] = max(triangle[r][c] + dp[r-1][c-1], triangle[r][c] + dp[r-1][c])

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))