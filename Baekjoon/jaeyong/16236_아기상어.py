# https://www.acmicpc.net/problem/16236
# 아기 상어

from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

class Shark:
    def __init__(self, y, x, size, cnt):
        self.y = y
        self.x = x
        self.size = size
        self.cnt = cnt

def bfs(y, x):
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append(Node(y, x))
    visited[y][x] = True

    temp = []

    while queue:
        node = queue.popleft()

        for d in range(4):
            ny = node.y + dy[d]
            nx = node.x + dx[d]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False:
                if board[ny][nx] <= shark.size:
                    queue.append(Node(ny, nx))
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[node.y][node.x] + 1

                    if board[ny][nx] < shark.size and board[ny][nx] != 0:
                        temp.append((ny, nx, distance[ny][nx]))

    # 물고기 먹는 우선순위 지정
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

# 처음 상어위치 찾기 / 상어 객체 생성
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = Shark(i, j, 2, 0)

result = 0
while True:
    s = bfs(shark.y, shark.x)

    # 더 이상 먹을 수 있는 물고기가 없는 경우 반복문 탈출
    if len(s) == 0:
        break

    ny, nx, dist = s.pop()

    # 시간 증가
    result += dist

    # 상어의 위치를 마지막으로 물고기를 먹은 위치로 이동시킨다
    board[shark.y][shark.x] = 0
    board[ny][nx] = 0

    shark.y = ny
    shark.x = nx
    shark.cnt += 1

    # 물고기를 충분히 먹은 경우 상어의 크기를 1 증가시킨다
    if shark.cnt == shark.size:
        shark.size += 1
        shark.cnt = 0
    
print(result)
