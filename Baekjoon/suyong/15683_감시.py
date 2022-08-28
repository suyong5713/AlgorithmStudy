#CCTV가 바라보는 방향을 #처리
def observe(x,y,dx,dy,checked_room):
  nx = x + dx
  ny = y + dy
  while 0 <= nx < N and 0 <= ny < M:
    #인덱스 유효성 검사와 벽 체크
    if checked_room[nx][ny] == 6:
      break
    checked_room[nx][ny] = "#"
    nx += dx
    ny += dy

def dfs(depth,checked_room):
  global min_invisible
  #depth는 처리한 cctv 개수를 의미
  if depth == len(cctv_list):
    invisible = 0
    for row in checked_room:
      invisible += row.count(0)
    min_invisible = min(invisible, min_invisible)
    return
  
  cctv_num, x, y = cctv_list[depth]
  #각 CCTV마다 회전했을때 바라보는 방향 경우의수가 다름
  for i in range(len(cctv_dir[cctv_num])):
    #python 함수의 매개변수는 항상 call by ref이므로 room 복사
    tempRoom = []
    for row in checked_room:
      tempRoom.append(row[:])
    #cctv_dir[현재 씨씨티비 번호][상,우,좌,하]
    #dir은 상, 우, 좌, 하 값 할당
    for index,dir in enumerate(cctv_dir[cctv_num][i]):
      if dir == 1:
        #dir 방향을 #으로 채움
        observe(x, y, dx[index],dy[index], tempRoom)
    #cctv가 특정 방향을 볼 때 상하좌우를 전부 처리 후 dfs
    dfs(depth+1, tempRoom)

N,M = list(map(int,input().split()))  
room = [list(map(int, input().split())) for _ in range(N)]
dx = [0,1,0,-1] #상우하좌
dy = [-1,0,1,0]
cctv_dir = [
  [],
  #cctv1
  [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
  #cctv2
  [[1,0,1,0],[0,1,0,1]],
  #cctv3
  [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]],
  #cctv4
  [[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]],
  #cctv5
  [[1,1,1,1]]
]
min_invisible = float("inf")
cctv_list = []
for i in range(N):
    for j in range(M):
      #cctv인 경우
      if 0 < room[i][j] < 6:
        #cctv번호,좌표 저장
        cctv_list.append([room[i][j],i,j])
dfs(0,room)
print(min_invisible)