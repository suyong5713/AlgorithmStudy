from itertools import combinations
from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs_init(active_virus, queue, visited):
    for vy, vx in active_virus:
        queue.append((vy, vx))
        visited[vy][vx] = True

def bfs(n, board, active_virus, empty_cnt, result):
    empty_chk = 0   # 현재 빈칸에 퍼트린 바이러스
    t = 0           # 시간

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    bfs_init(active_virus, queue, visited)

    while True:
        # 1초동안 새로 생성된 바이러스 수
        queue_size = len(queue)

        # 빈 칸이 모두 없어진 경우
        if empty_cnt == 0:
            return 0
        
        # 빈 칸을 모두 채웠다면 시간 반환
        if empty_chk == empty_cnt:
            return t
        
        # 더 이상 탐색할 수 없으나, 빈 칸이 남아있는 경우 (바이러스 퍼트리기 불가)
        if empty_cnt != 0 and queue_size == 0:
            return sys.maxsize
        
        # 1초동안 시간이 흐름
        t += 1

        # 기존 탐색한 시간보다 더 걸리는 경우
        if t > result:
            return sys.maxsize

        # 1초동안 돌아야 할 큐 길이만큼만 반복
        for _ in range(queue_size):
            ny, nx = queue.popleft()
            
            for d in range(4):
                y = ny + dy[d]
                x = nx + dx[d]

                if 0 <= y < n and 0 <= x < n and board[y][x] != 1 and visited[y][x] == False:
                    if board[y][x] == 0:
                        queue.append((y, x))
                        empty_chk += 1

                    elif board[y][x] == 2:
                        queue.append((y, x))
                    
                    visited[y][x] = True

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

empty_cnt = 0
virus_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            empty_cnt += 1
        elif board[i][j] == 2:
            virus_list.append((i, j))

result = sys.maxsize
for active_virus in combinations(virus_list, m):
    r = bfs(n, board, active_virus, empty_cnt, result)
    result = min(result, r)

print(-1 if result == sys.maxsize else result)
