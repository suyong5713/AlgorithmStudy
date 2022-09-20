def BFS(row,col,color):
  visited = [[False] * N for _ in range(N)]
  group = [[row,col]]
  queue = [[row,col]]
  visited[row][col] = True
  while queue:
    row, col = queue.pop(0)
    for dir in range(4):
      n_row = row + d_row[dir]
      n_col = col + d_col[dir]
      if 0 <= n_row < N and 0 <= n_col < N:
        #같은색 블럭 or 무지개블럭
        if grid[n_row][n_col] == color or grid[n_row][n_col] == 0:
          if not visited[n_row][n_col]:
            visited[n_row][n_col] = True
            queue.append([n_row,n_col])
            group.append([n_row,n_col])
  return group
def gravity():
  for i in range(N-2,-1,-1):
    for j in range(N):
      #검정블록이 아니면
      if grid[i][j] > -1:
        n_row = i+1
        #아래칸이 빈칸이 아닐때 까지 중력 작용
        while True:
          if n_row < N and grid[n_row][j] == -2:
            n_row += 1 
          else: 
            n_row -= 1
            break
        temp = grid[i][j]
        grid[i][j] = -2
        grid[n_row][j] = temp
  return
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
score = 0
d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
while True:
  max_size, max_rainbow = 0,0
  #파괴시킬 블럭 그룹
  block_group = []
  #이미 한번 그룹화된 블럭
  grouped = []
  for i in range(N):
    for j in range(N):
      #방문한 적 없는 일반블럭 선택
      if grid[i][j] > 0 and [i,j] not in grouped:
        group = BFS(i, j, grid[i][j])
        if len(group) < 2:
          continue
        grouped.extend(group)
        rainbow_block = 0
        for k in range(len(group)):
            row,col = group[k]
            #무지개 블럭
            if grid[row][col] == 0:
              rainbow_block += 1
        if len(group) > max_size:
          max_size = len(group)
          block_group = group
          max_rainbow = rainbow_block
        #블록그룹 길이가 같으면 무지개 블럭이 많은게 우선
        elif len(group) == max_size:
          if rainbow_block >= max_rainbow:
            max_rainbow = rainbow_block
            block_group = group
  if max_size < 2:
    break
  score += max_size * max_size
  for block in block_group:
    row,col = block
    grid[row][col] = -2
  gravity()
  grid = list(map(list,zip(*grid)))[::-1]
  gravity()
print(score)