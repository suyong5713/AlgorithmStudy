# https://www.acmicpc.net/problem/2638
# 치즈, BFS

from collections import deque

EMPTY   = 0
CHEESE  = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board):
    time = 0
    queue = deque()

    while True:
        # 이번 time에서 치즈를 녹인 개수
        cnt = 0

        # 가장자리부터 공기를 확산시킴
        queue.append((0, 0))
        visited = [[0] * m for _ in range(n)]
        
        while queue:
            ny, nx = queue.popleft()

            for d in range(4):
                y = ny + dy[d]
                x = nx + dx[d]

                if 0 <= y < n and 0 <= x < m:
                    if board[y][x] == EMPTY and visited[y][x] == 0:
                        queue.append((y, x))
                        visited[y][x] = 1

                    if board[y][x] == CHEESE and visited[y][x] < 2:
                        visited[y][x] += 1
            
                        # 치즈가 녹는 조건에 부합하는 경우
                        if visited[y][x] == 2:
                            board[y][x] = EMPTY
                            cnt += 1
        
        # 녹일 수 있는 치즈가 더 이상 없는 경우
        if cnt == 0:
            return time
        
        time += 1
                  
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, m, board)
print(result)
