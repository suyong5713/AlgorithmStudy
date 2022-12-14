def matrix(x, y):
    xx, yy = x, y
    row, column = 1, 1

    while True:
        x += 1
        if x < n and arr[x][y] != 0 and not visited[x][y]:
            row += 1
        else:
            x -= 1
            break
    while True:
        y += 1
        if y < n and arr[x][y] != 0 and not visited[x][y]:
            column += 1
        else:
            y -= 1
            break

    for i in range(xx, x + 1):
        for j in range(yy, y + 1):
            visited[i][j] = True

    return [row, column]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and not visited[i][j]:
                value = matrix(i, j)
                result.append(value)

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print("#{} {}".format(tc, len(result)), end=' ')
    for r in result:
        print("{} {}".format(r[0], r[1]), end=' ')
    print()