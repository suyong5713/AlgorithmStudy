def dfs(depth, score):
    global max_score
    # 주사위 10개의 수를 모두 탐색했다면 최댓값 비교 후 리턴
    if depth == 10:
        max_score = max(max_score, score)
        return

    # 4개의 말에 대해 백트래킹
    for i in range(4):
        # pos와 now는 현재 말의 위치(pos는 변화할 값), num은 주사위값
        pos, now, num = horse[i], horse[i], numbers[depth]

        # 말이 5, 10, 15 위치에 있다면 파란선을 따라 가야하므로 pos 각각 갱신하고 주사위값 1 빼주기
        if pos in [5, 10, 15]:
            if pos == 5:
                pos = 22
            elif pos == 10:
                pos = 25
            else:
                pos = 27
            num -= 1

        # 주사위값만큼 반복해주면서 위치 갱신해주기
        for _ in range(num):
            pos = connect[pos]

        # 갱신된 위치가 도착지점이 아닌데 그 지점에 다른 말이 있다면 백트래킹 안하고 반복문 다시 돌게함
        if visited[pos] and pos != 21:
            continue

        # 백트래킹
        visited[now], visited[pos], horse[i] = False, True, pos
        dfs(depth+1, score + score_list[pos])
        visited[now], visited[pos], horse[i] = True, False, now


numbers = list(map(int, input().split()))

# 연결 정보 저장 -> ex : 1번 노드의 경우 2번 노드와 연결, 22번 노드의 경우 23번 노드와 연결
# 인덱스 어떻게 되어 있는지는 readme 확인해주세요
connect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 21, 23, 24, 30, 26, 30, 28, 29, 30,
          31, 32, 20]

# 점수 정보 저장 -> ex : 5번 노드의 경우 10점
score_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 0, 13, 16, 19, 22, 24, 28, 27, 26,
         25, 30, 35]

horse = [0, 0, 0, 0]
visited = [False for _ in range(33)]

max_score = 0
dfs(0, 0)

print(max_score)