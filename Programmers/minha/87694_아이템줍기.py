from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    answer = 0
    board = [[-1] * 101 for _ in range(101)]

    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                board[i][j] = 0

    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                board[i][j] = -1

    cx = 2 * character_x
    cy = 2 * character_y
    ix = 2 * item_x
    iy = 2 * item_y

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False] * 101 for _ in range(101)]
    visited[cx][cy] = True

    q = deque([(cx, cy)])

    while q:
        x, y = q.popleft()

        if x == ix and y == iy:
            answer = board[x][y] // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 101 and 0 <= ny < 101 and board[nx][ny] > -1 and not visited[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

    return answer

print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))