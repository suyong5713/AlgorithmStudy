N, M = map(int, input().split())
maze = [list(map(str, input())) for _ in range(N)]
visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
queue = []

for i in range(N):
    for j in range(M):
        if maze[i][j] == "0":
            maze[i][j] = "."
            queue.append((i, j, 0))
            break
answer = -1
while queue:
    x, y, key = queue.pop(0)
    for dir in [[0, 1], [1,0], [-1,0], [0,-1]]:
        n_row = x + dir[0]
        n_col = y + dir[1]
        new_key = key
        # 범위 안 이면서 벽도 아니고 동일한 키를 가지고 그곳에 방문한 적이 없어야 한다.
        if (
            0 <= n_row < N
            and 0 <= n_col < M
            and maze[n_row][n_col] != "#"
            # 같은 키를 들고 재방문 불가능. 새로운 키를 얻으면 재방문 가능
            and visited[n_row][n_col][key] == 0
        ):

            if maze[n_row][n_col].isupper():
                if not (key & 1 << (ord(maze[n_row][n_col]) - ord("A"))):
                    # "D"일경우 1 << 3 = 1000. 키 d를 가지고 있는지 and 연산으로 확인
                    continue
            elif maze.islower():
                # 'd'일 경우 1 << 3 = 1000. 현재 키가 0001 이라고 한다면(a만 소지) or 연산으로 키 합치기.
                new_key |= 1 << ord(maze[n_row][n_col]) - ord("a")
            # 출구 찾으면
            elif maze[n_row][n_col] == "1":
                answer = visited[n_row][n_col][key] + 1
                break
            queue.append((n_row, n_col, new_key))
            visited[n_row][n_col][new_key] = visited[x][y][key] + 1
print(answer)
