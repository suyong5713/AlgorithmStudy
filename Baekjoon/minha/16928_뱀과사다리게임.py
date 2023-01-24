from collections import deque

def is_ladder_snake(p):
    for start, end in ladder_or_snake:
        if p == start:
            return end

    return 0

N, M = map(int, input().split())
ladder_or_snake = [list(map(int, input().split())) for _ in range(N + M)]
visited = [False] * 101

q = deque()
q.append((1, 0))
visited[0] = visited[1] = True

while q:
    c_pos, c_move = q.popleft()
    for i in range(1, 7):
        n_pos = c_pos + i
        if n_pos == 100:
            print(c_move + 1)
            exit()
        if 1 <= n_pos <= 100 and not visited[n_pos]:
            res = is_ladder_snake(n_pos)
            if res > 0:
                visited[res] = True
                q.append((res, c_move + 1))
            else:
                q.append((n_pos, c_move + 1))