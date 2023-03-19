# https://www.acmicpc.net/problem/1987
# 알파벳, DFS

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
board = [[(ord(j) - 65) for j in input()] for _ in range(r)]

queue = deque()
visited = [False] * 26

queue.append((0, 0, 1))
visited[board[0][0]] = True

# 최초 (0, 0) 위치에 대한 길이도 포함
result = 1

def dfs():
    global r, c, result

    while queue:
        ny, nx, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < r and 0 <= x < c and visited[board[y][x]] == False:
                queue.append((y, x, nt + 1))
                visited[board[y][x]] = True

                result = max(result, nt + 1)
                dfs()

                visited[board[y][x]] = False

dfs()
print(result)
