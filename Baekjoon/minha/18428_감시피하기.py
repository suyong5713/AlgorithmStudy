dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 직선 방향 확인
def check(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        while 0 <= ny < N and 0 <= nx < N and graph[ny][nx] != 'O':
            if graph[ny][nx] == 'S':
                return True
            else:
                ny += dy[i]
                nx += dx[i]

    return False


def dfs(depth):
    global flag

    if depth == 3:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'T':
                    if not check(i, j):
                        cnt += 1

        if cnt == teacher_cnt:
            flag = True
        return

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(depth + 1)
                graph[i][j] = 'X'


N = int(input())
graph = [list(map(str, input().split())) for _ in range(N)]

teacher_cnt = sum(graph, []).count('T')
flag = False

dfs(0)

if flag:
    print("YES")
else:
    print("NO")
