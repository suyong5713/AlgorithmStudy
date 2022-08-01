from collections import deque
import sys
input = sys.stdin.readline


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []    # 구슬 방문 여부
    visited.append((rx, ry, bx, by))
    cnt = 0     # 횟수
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            # 횟수가 10회 초과
            if cnt > 10:
                return -1
            if graph[rx][ry] == 'O':
                return cnt
            for i in range(4):
                # 빨간 구슬 이동
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    # 장애물에 부딪혔을 때
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    # 구멍에 도달했을 때
                    if graph[nrx][nry] == 'O':
                        break
                # 파란 구슬 이동
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    # 장애물에 부딪혔을 때
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    # 구멍에 도달했을 때
                    if graph[nbx][nby] == 'O':
                        break
                # 파란 구슬이 구멍에 빠졌을 경우 => 원하는 답이 아니므로 다음 경우로 가기 위해 continue
                if graph[nbx][nby] == 'O':
                    continue
                # 두 구슬의 위치가 같을 경우
                if nrx == nbx and nry == nby:
                    # 더 이동한 길이가 긴 구슬이 뒤쪽에 있던 구슬이므로 한 칸 뒤로 이동
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        # 빨간 구슬 위치
        if graph[i][j] == 'R':
            rx, ry = i, j
        # 파란 구슬 위치
        elif graph[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by))