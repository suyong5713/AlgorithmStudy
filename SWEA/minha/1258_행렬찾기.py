def matrix(x, y) :
    sx, sy = x, y
    row = 1
    col = 1

    while True :
        x += 1
        if x < n and graph[x][y] != 0 :
            row += 1
        else :
            x -= 1
            break
    while True :
        y += 1
        if y < n and graph[x][y] != 0 :
            col += 1
        else :
            y -= 1
            break

    # 한 행, 한 열만 보는거라 위에서 graph = 0 하면 소용 없음
    # 범위 지정해서 해당 범위 graph = 0 해줘야 함
    for i in range(sx, sx + row):
        for j in range(sy, sy + col):
            graph[i][j] = 0

    return [row, col]

t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for i in range(n) :
        for j in range(n) :
            if graph[i][j] != 0 :
                result.append(matrix(i, j))

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print("#{} {}".format(tc, len(result)), end=' ')
    for r in result :
        print(r[0], r[1], end=' ')
    print()