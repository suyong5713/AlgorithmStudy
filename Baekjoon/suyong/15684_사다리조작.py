N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
ans = 4

for i in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1


def move():
    for n in range(N):
        start = n
        for h in range(H):
            if ladder[h][start]:  # 우측이동
                start += 1
            elif start > 0 and ladder[h][start - 1]:  # 좌측이동
                start -= 1
        if start != n:
            return False
    return True


def dfs(cnt, row, col):
    global ans
    if ans <= cnt:
        return
    if move():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    #H: 3일 때
    for i in range(row, H):
        if i == row: k = col
        else: k = 0
        for j in range(k, N - 1):
            if ladder[i][j]:
                continue
            else:
                #사다리 추가
                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                #백트래킹
                ladder[i][j] = 0

dfs(0, 0, 0)
print(ans if ans < 4 else -1)