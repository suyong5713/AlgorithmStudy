def observe(x,y,dx,dy,checked_room):
  nx = x + dx
  ny = y + dy
  while 0 <= nx < N and 0 <= ny < M:
    if checked_room[nx][ny] == 6:
      break
    checked_room[nx][ny] = "#"
    nx += dx
    ny += dy

def dfs(depth,checked_room):
  global min_invisible
  if depth == len(cctv_list):
    invisible = 0
    for row in checked_room:
      invisible += row.count(0)
    min_invisible = min(invisible, min_invisible)
    return
  cctv_num, x, y = cctv_list[depth]
  for i in range(len(cctv_dir[cctv_num])):
    tempRoom = []
    for row in checked_room:
      tempRoom.append(row[:])
    for index,dir in enumerate(cctv_dir[cctv_num][i]):
      if dir == 1:
        observe(x, y, dx[index],dy[index], tempRoom)
    dfs(depth+1, tempRoom)

N,M = list(map(int,input().split()))  
room = [list(map(int, input().split())) for _ in range(N)]
dx = [0,1,0,-1] #상우하좌
dy = [-1,0,1,0]
cctv_dir = [
  [],
  [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
  [[1,0,1,0],[0,1,0,1]],
  [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]],
  [[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]],
  [[1,1,1,1]]
]
min_invisible = float("inf")
cctv_list = []
for i in range(N):
    for j in range(M):
      #cctv인 경우
      if 0 < room[i][j] < 6:
        cctv_list.append([room[i][j],i,j])
dfs(0,room)
print(min_invisible)