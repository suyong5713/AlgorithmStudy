N, M, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
shark_pos = [0] * (M + 1)
#상어의 위치 저장하면서 격자를 2차원 -> 3차원 변환
for i in range(N):
  for j in range(N):
    if grid[i][j] > 0:
      shark_pos[grid[i][j]] = [i,j]
      grid[i][j] = [grid[i][j]]
    else:
      grid[i][j] = []
#냄새를 표현할 3차원 배열
smell_map = [[[0,0] for _ in range(N)] for _ in range(N)]
#상어의 방향 정보
shark_dir = list(map(int,input().split()))
#상 하 좌 우. 인덱스 맞추기
direction = [[0],[-1,0], [1,0], [0,-1], [0,1]]
#각 상어의 이동방향 별 우선순위 정보
shark_priority = [[] for _ in range(M)]
#상어 M마리의 우선순위 정보 저장
for i in range(M):
  for _ in range(4):
    shark_priority[i].append(list(map(int,input().split())))
#인덱스 맞추기
shark_dir.insert(0, 0)
shark_priority.insert(0,0)
#초기화. 자신의 위치에 냄새 뿌림.
for i in range(N):
  for j in range(N):
    if len(grid[i][j]) > 0:
      #상어번호, 냄새 수명
      smell_map[i][j] = [grid[i][j][0], K]
time = 0
#격자에 존재하는 상어 번호 리스트
exist_shark = []
for i in range(1, M + 1):
  exist_shark.append(i)
while True: # 1번 상어만 남거나, 1000초 이상 넘어가면 중지
  if time > 1000: 
    print(-1)
    break
  elif len(exist_shark) == 1: 
    print(time)
    break
  time += 1
  #상어 위치정보를 하나씩 빼서 이동시킴
  for s in range(1,len(shark_pos)):
    #반복문에서 뽑은 상어가 격자내에 존재하지 않으면 continue
    if s not in exist_shark:
      continue
    shark_num = s
    row, col = shark_pos[s]
    isMoved = False
    #인접한 칸 이동.
    #현재 상어의 이동방향에 따른 우선순위로 4방탐색
    #shark_priority[상어번호][상어의 이동방향 - 1] -> [이동방향 우선순위]
    for dir in shark_priority[shark_num][shark_dir[shark_num] - 1]:
      dr, dc = direction[dir]
      nr, nc = row + dr, col + dc
      #격자 내에 냄새가 없는 칸이 있으면 이동.
      if 0 <= nr < N and 0 <= nc < N and smell_map[nr][nc] == [0,0]:
        grid[nr][nc].append(shark_num)
        #원래있던 위치에서 상어를 제거.
        grid[row][col].pop(grid[row][col].index(shark_num))
        #이동한 방향에 따라 상어의 방향, 위치 정보 갱신
        shark_dir[shark_num] = dir
        shark_pos[shark_num] = [nr,nc]
        isMoved = True
        break
    #냄새가 없는칸이 없어서 이동을 못했다면.
    if not isMoved:
      for dir in shark_priority[shark_num][shark_dir[shark_num] - 1]:
        dr, dc = direction[dir]
        nr, nc = row + dr, col + dc
        #격자 내의 자신의 냄새가 있는 칸으로 이동. 이것도 없으면 이동 못함
        if 0 <= nr < N and 0 <= nc < N and smell_map[nr][nc][0] == shark_num:
          grid[nr][nc].append(shark_num)
          grid[row][col].pop(grid[row][col].index(shark_num))
          #방향, 위치 갱신
          shark_dir[shark_num] = dir
          shark_pos[shark_num] = [nr,nc]
          break
  #모든 상어가 이동 가능한 곳으로 이동완료.
  #같은 칸에 상어가 여럿 있다면 가장 낮은 번호 상어만 남기고 소멸
  #현재 격자에 남아있는 상어를 담을 리스트.
  shark_list = []
  for i in range(N):
    for j in range(N):
      #smell_map[row][col] -> [상어 번호, 냄새 수명]
      if smell_map[i][j][0] > 0:
        smell_map[i][j][1] -= 1
        #냄새 수명이 0이되면 냄새의 상어 번호도 삭제.
        if smell_map[i][j][1] == 0:
          smell_map[i][j] = [0,0]
      #한 칸에 두마리 이상의 상어가 있다면
      if len(grid[i][j]) > 1:
        #번호가 가장 작은 상어 제외하고 제거.
        grid[i][j] = [min(grid[i][j])]
      #칸에 있는 상어의 냄새 뿌림
      if len(grid[i][j]) > 0:
        #격자에 존재하는 상어 리스트에 현재 상어 추가.
        shark_list.append(grid[i][j][0])
        #냄새 저장.
        smell_map[i][j] = [grid[i][j][0], K]
  #격자에 존재하는 상어 갱신.
  exist_shark = shark_list