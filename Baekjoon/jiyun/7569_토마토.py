from collections import deque
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]

def checkAns() -> int:
    ans = 0
    for i in arr:
        for j in i:
            if not j:            # 토마토 없는 경우
                return -1
        ans = max(ans, max(i))
    return ans - 1

def bfs():
    while queue:
        x, y = queue.popleft()
        for move in MOVES:
            nx, ny = move[0] + x, move[1] + y
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:     # 좌표 내 & 토마토 익힘 X
                arr[nx][ny] = arr[x][y] + 1                         # 토마토 익힘 O
                queue.append([nx, ny])
    return checkAns()

def getTomatoInfo() -> deque:
    _queue = deque([])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                _queue.append([i, j])
    return _queue

if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    queue = getTomatoInfo()
    print(bfs())

