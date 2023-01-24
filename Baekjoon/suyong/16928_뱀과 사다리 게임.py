N, M = map(int,input().split())
board = [[0, 0] for _ in range(101)]

# 0번째 인덱스에는 사다리 출구, 1번째 인덱스에는 뱀 출구 저장
for _ in range(N):
    x, y = map(int,input().split())
    board[x][0] = y
for _ in range(M):
    u, v = map(int, input().split())
    board[u][1] = v
visited = [0] * 101
queue = [1]
visited[1] = 1
while queue:
    current = queue.pop(0)
    for dice in range(1, 7):
        next = current + dice
        if 0 < next <= 100 and not visited[next]:
            # 사다리 있는지 확인
            if board[next][0]:
                next = board[next][0]
            # 뱀이 있는지 확인
            if board[next][1]:
                next = board[next][1]
            if not visited[next]:
                queue.append(next)
                visited[next] = visited[current] + 1
print(visited[100] - 1)