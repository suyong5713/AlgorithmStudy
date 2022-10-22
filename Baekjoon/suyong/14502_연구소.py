from argparse import ZERO_OR_MORE
from copy import deepcopy
from itertools import combinations

def BFS(lab,pos, visited):
  global max_zero_count
  queue = [pos]
  visited[pos[0]][pos[1]] = True
  zero_count = 0
  for row in lab:
    zero_count += row.count(0)
  while queue:
    row, col = queue.pop(0)
    for dir in range(4):
      nrow = row + drow[dir]
      ncol = col + dcol[dir]
      if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and lab[nrow][ncol] == 0:
        visited[nrow][ncol] = True
        lab[nrow][ncol] = 2
        queue.append([nrow,ncol])
        zero_count -= 1
        if zero_count <= max_zero_count:
          return

  return
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
N, M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]
#빈공간 좌표 중 3개 선택해서 벽 세우기
blank_list = []
for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      blank_list.append([i, j])
comb = list(combinations(blank_list, 3))
max_zero_count = 0
for combination in comb:
  copied_lab = deepcopy(lab)
  for row, col in combination:
    copied_lab[row][col] = 1
  visited = [[False] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if copied_lab[i][j] == 2 and not visited[i][j]:
        BFS(copied_lab, [i,j], visited)
  zero_count = 0
  for row in copied_lab:
    zero_count += row.count(0)
  max_zero_count = max(max_zero_count,zero_count)
print(max_zero_count)