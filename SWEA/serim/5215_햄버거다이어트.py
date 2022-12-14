def dfs(index, score, cal):
    global max_score    # 결과 => 최대 점수
    # 칼로리가 입력받은 제한 칼로리보다 높으면 return
    if cal > L:
        return
    # 현재 점수가 최대 점수보다 높으면 최대 점수에 넣어줌
    if max_score < score:
        max_score = score
    # 현재 재료의 인덱스 == 재료 수 이면 인덱스에 해당하는 재료가 없으므로 return
    if index == N:
        return
    # 현재 인덱스에 해당하는 재료를 넣지 않을 경우
    dfs(index + 1, score, cal)
    # 현재 인덱스에 해당하는 재료를 넣을 경우
    dfs(index + 1, score + ingredients[index][0], cal + ingredients[index][1])

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    max_score = 0
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    dfs(0, 0, 0)
    print("#{} {}".format(test_case, max_score))