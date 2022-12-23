def border(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for dir in [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [0, -1]]:
                    n_row, n_col = i + dir[0], j + dir[1]
                    if 0 <= n_row < n and 0 <= n_col < n and grid[n_row][n_col] == 0:
                        grid[i][j] = 2
                        break
    return


def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    n = 0
    # 사각형 우상단 최댓값 구하기.
    for rect in rectangle:
        n = max(n, max(rect[2:]))
    n = (n * 2) + 2
    grid = [[0] * n for _ in range(n)]
    for rect in rectangle:
        left_x, left_y, right_x, right_y = map(lambda x: x * 2, rect)
        for i in range(left_y, right_y + 1):
            for j in range(left_x, right_x + 1):
                grid[i][j] = 1
    border(grid, n)
    stack = [[characterX, characterY, 0]]
    visited = [[False] * n for _ in range(n)]
    visited[characterY][characterX] = True
    answer = float('inf')
    while stack:
        col, row, distance = stack.pop()
        if [col, row] == [itemX, itemY]:
            answer = min(answer, distance)
            visited[row][col] = False
            continue
        for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            n_row, n_col = row + dir[0], col + dir[1]
            if 0 <= n_row < n and 0 <= n_col < n and not visited[n_row][n_col] and grid[n_row][n_col] == 2:
                visited[n_row][n_col] = True
                stack.append([n_col, n_row, distance + 1])
    answer = answer // 2
    return answer