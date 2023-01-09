def solution(triangle):
    # 삼각형의 수를 더해서 저장할 dp 생성
    dp = [[0] * (len(triangle)) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for idx, j in enumerate(triangle[i]):
            # 현재 경로까지의 숫자 합 = 이전 경로까지의 숫자합 + 현재 숫자
            # 더하는 수 : 이전 행의 현재 [인덱스 - 1] or 이전행의 [현재인덱스]
            dp[i][idx] = triangle[i][idx] + max(dp[i - 1][idx - 1], dp[i - 1][idx])
    answer = max(dp[-1])
    return answer