for test_case in range(1, 11):
    n = int(input())
    graph = [list(input()) for _ in range(8)]
    cnt = 0
    # 가로
    for i in range(8):
        for j in range(9 - n):
            if graph[i][j:j + n] == graph[i][j:j + n][::-1]:
                cnt += 1
    # 세로
    for j in range(8):
        for i in range(9 - n):
            ch = ''
            for k in range(i, i + n):
                ch += graph[k][j]
            if ch == ch[::-1]:
                cnt += 1

    print("#{} {}".format(test_case, cnt))