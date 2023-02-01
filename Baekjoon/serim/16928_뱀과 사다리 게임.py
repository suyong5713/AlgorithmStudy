from collections import deque

def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        if x == 100:
            print(board[x])
            exit(0)
        for num in range(1, 7):
            nx = x + num
            if nx <= 100 and not visited[nx]:
                if nx in ladders.keys():
                    nx = ladders[nx]
                elif nx in snakes.keys():
                    nx = snakes[nx]
                if not visited[nx]:
                    visited[nx] = 1
                    board[nx] = board[x] + 1
                    queue.append(nx)

n, m = map(int, input().split())
ladders, snakes = {}, {}
for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b
board = [0] * 101
visited = [0] * 101
bfs()