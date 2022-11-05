def dfs(y, x, tot):
    global answer

    if x == M:
        y += 1
        x = 0

    if y == N:
        answer = max(answer, tot)
        return

    if not visited[y][x]:
        for i in range(4):
            fny = y + shape[i][0]
            fnx = x + shape[i][1]
            sny = y + shape[i][2]
            snx = x + shape[i][3]

            if 0 <= fny < N and 0 <= fnx < M and 0 <= sny < N and 0 <= snx < M:
                if not visited[fny][fnx] and not visited[sny][snx]:
                    visited[y][x] = True
                    visited[fny][fnx] = True
                    visited[sny][snx] = True
                    boomerang = 2 * material[y][x] + material[fny][fnx] + material[sny][snx]
                    dfs(y, x + 1, tot + boomerang)
                    visited[y][x] = False
                    visited[fny][fnx] = False
                    visited[sny][snx] = False

    dfs(y, x + 1, tot)
    return

N, M = map(int, input().split())
material = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
shape = [[0, -1, 1, 0], [0, -1, -1, 0], [-1, 0, 0, 1], [1, 0, 0, 1]]

answer = 0
dfs(0, 0, 0)

print(answer)