T = int(input())
for test_case in range(1, T + 1):
    # N : 음식의 개수, L : 최대 칼로리
    N, L = map(int, input().split())
    recipe = [[0,0]] # 음식이 아무것도 포함되지 않은 초기 상태 설정

    for i in range(N):
        # 음식 배열에 추가
        recipe.append(list(map(int, input().split())))

    # 행 : 음식의 개수+1, 열 : 칼로리+1인 표를 0으로 초기화
    dp = [ [0]*(L+1) for _ in range(N+1) ]

    for item in range(1, N+1): # 행
        for cur_calorie in range(1, L+1): # 열

            calorie = recipe[item][1] # 현재 j 번째의 음식의 칼로리
            score = recipe[item][0] # 현재 j 번째의 음식의 점수 지정

            if (cur_calorie < calorie): # 음식이 현재의 최대 칼로리보다 클 때
                # 음식을 넣지 않는다, 이전 음식으로 처리
                dp[item][cur_calorie] = dp[item-1][cur_calorie]
            else:
                # 더 나은 경우를 찾는다.
                # S1. 현재 음식을 넣지 않는다.
                # S2. 현재 음식을 넣기 위헤, 칼로리 값을 빼고 음식을 넣기
                dp[item][cur_calorie] = max(dp[item-1][cur_calorie], dp[item-1][cur_calorie-calorie] + score)

    print("#{} {}".format(test_case, dp[N][L]))