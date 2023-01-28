import sys
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
answer = 0
# for d_height, d_row, d_col in [[0,0,1], [0,0,-1]...] 방식보다 빠름
d_height = [-1,1,0,0,0,0]
d_row = [0,0,-1,1,0,0]
d_col = [0,0,0,0,-1,1]

for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                queue.append((h, r, c))
while queue:
    h, r, c = queue.popleft()

    for i in range(6):
        n_height = h + d_height[i]
        n_row = r + d_row[i]
        n_col = c + d_col[i]
        # 범위 체크
        if n_height < 0 or n_height >= H or n_row < 0 or n_row >= N or n_col < 0 or n_col >= M:
            continue
        # 토마토가 아직 익지 않았고 방문한 적 없을 때.
        if box[n_height][n_row][n_col] == 0:
            queue.append((n_height, n_row, n_col))
            box[n_height][n_row][n_col] = box[h][r][c] + 1
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)
# 덱과 리스트 시간복잡도 차이.
# https://wellsw.tistory.com/122