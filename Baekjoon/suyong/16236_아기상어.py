def BFS(row, col):
  visited = [[0] * N for _ in range(N)]
  #방문여부와 이동거리 동시에 표현
  #0은 미방문. 기본 1부터시작. 따라서 실제 반환하는 값은 -1해서 반환.
  visited[row][col] = 1
  queue = [[row, col]]
  fish_list = []
  while queue:
    r, c = queue.pop(0)
    for dir in range(4):
      next_row, next_col = r + drow[dir], c + dcol[dir]
      if 0 <= next_row < N and 0 <= next_col < N and visited[next_row][next_col] == 0:
        #물고기가 있고 사이즈가 상어보다 작을때
        if shark_size[0] > room[next_row][next_col] and room[next_row][next_col] != 0:
            visited[next_row][next_col] =  visited[r][c] + 1
            #이동거리를 1부터 시작했으므로 1빼서 저장.
            fish_list.append((visited[next_row][next_col] - 1, next_row, next_col))
        #물고기 크기가 상어와 동일할 때. 이동만 가능
        elif shark_size[0] == room[next_row][next_col]:
            visited[next_row][next_col] =  visited[r][c] + 1
            queue.append([next_row, next_col])
        #물고기가 없을때 그냥 이동.
        elif room[next_row][next_col] == 0:
            visited[next_row][next_col] =  visited[r][c] + 1
            queue.append([next_row,next_col])
  return sorted(fish_list, key=lambda x: (x[0],x[1],x[2]))
N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
drow = [-1,1,0,0]
dcol = [0,0,-1,1]

#상어 크기와 먹은 물고기 수
shark_pos = []
shark_size = [2,0]
for i in range(N):
  for j in range(N):
    if room[i][j] == 9:
      shark_pos = [i,j]
      break
time = 0

while True:
  result_list = BFS(shark_pos[0], shark_pos[1])
  #먹을수 있는 고기가 없으면
  if not result_list:
    break
  #거리, 물고기 위치
  dist, row, col = result_list.pop(0)
  #시간 증가
  time += dist
  shark_size[1] += 1
  #덩치만큼 고기 먹으면 크기 성장
  if shark_size[0] == shark_size[1]:
    shark_size[0] += 1
    shark_size[1] = 0
  #물고기 먹힘
  room[row][col] = 0
  #상어가 있던 위치 0.
  room[shark_pos[0]][shark_pos[1]] = 0
  #상어 이동
  shark_pos = [row,col]
print(time)