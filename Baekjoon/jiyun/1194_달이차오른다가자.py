
from collections import deque

MOVE =[(-1,0),(0,1),(1,0),(0,-1)]


def solution() :
    answer = -1
    while queue:
        x, y, n_value = queue.popleft()
        for move in MOVE:
            nx = x + move[0]
            ny = y + move[1]
            nn_value = n_value
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != "#" and not visited[nx][ny][n_value]:
                if arr[nx][ny].isupper():
                    if not (n_value & 1 << (ord(arr[nx][ny]) - ord("A"))):
                        continue
                elif arr[nx][ny].islower():
                    nn_value |= 1 << ord(arr[nx][ny]) - ord("a")
                elif arr[nx][ny] == "1":
                    answer = visited[x][y][n_value] + 1
                    return answer
                queue.append((nx, ny, nn_value))
                visited[nx][ny][nn_value] = visited[x][y][n_value] + 1
    return answer


n, m = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(n)]
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == "0":
            arr[i][j] = "."
            queue.append((j, i, 0))
            break
            
print(solution())
            
            