from collections import deque

N, M = map(int, input().split())

ladder_or_snake = dict()
for _ in range(N + M):
    start, end = map(int, input().split())
    ladder_or_snake[start] = end

visited = [False] * 101
q = deque()
q.append((1, 0))
visited[1] = True

while q:
    c_pos, c_move = q.popleft()
    for i in range(1, 7):
        n_pos = c_pos + i
        if n_pos == 100:
            print(c_move + 1)
            exit()
        if 1 <= n_pos <= 100 and not visited[n_pos]:
            if n_pos in ladder_or_snake.keys():
                visited[n_pos] = True
                q.append((ladder_or_snake[n_pos], c_move + 1))
            else:
                visited[n_pos] = True
                q.append((n_pos, c_move + 1))