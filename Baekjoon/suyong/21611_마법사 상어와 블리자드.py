def move(distance,d_row,d_col):
    global shark_r,shark_c
    #상어 위치를 기준으로 회오리모양 인덱싱
    #gird를 선형으로 변환
    for _ in range(distance):
        shark_r += d_row
        shark_c += d_col
        if 0 <= shark_r < N and 0 <= shark_c < N:
            grid_indexing.append((shark_r,shark_c))
            beads.append(grid[shark_r][shark_c])
    return
def beadsMove():
    index = 0
    #블리자드로 파괴된 구슬(-1)을 빼서 리스트마지막에 0으로 삽입
    while index != len(beads):
        if beads[index] == -1:
            beads.pop(index)
            beads.append(0)
        else: index += 1
    #구슬배열의 변화를 grid에 반영
    for i in range(N*N-1):
        row, col = grid_indexing[i]
        grid[row][col] = beads[i]
def blizzard(row, col, dir, dist):
  #row, col 위치에서 dir 방향으로 dist거리만큼 파괴
    for _ in range(dist):
        row += direction[dir][0]
        col += direction[dir][1]
        grid[row][col] = -1
        #grid의 변화를 구슬배열에도 반영
        beads[grid_indexing.index((row,col))] = -1
def explosion():
  flag = False
  start, end = 0, 0
  #현재 구슬의 숫자 num
  num = beads[0]
  for i in range(len(beads)):
    #숫자가 변하면 start~end길이가 4보다 큰지 확인하고 파괴
    if num != beads[i]:
      #새로운 숫자를 num에 저장
      num = beads[i]
      end = i
      if end - start >= 4:
        #파괴된 구슬 개수 저장
        explosed_beads[beads[start]-1] += end-start
        for j in range(start, end):
          beads[j] = -1
          #한번이라도 파괴되면 플래그 True
          flag = True
      #바뀐숫자 시작 인덱스 start
      start = i
  #구슬의 변화를 격자에 반영
  for i in range(N*N-1):
    row, col = grid_indexing[i]
    grid[row][col] = beads[i]
  return flag
def beadsChange():
  global beads
  start,end = 0,0
  num = beads[0]
  changed_beads = []
  for i in range(len(beads)):
    #숫자가 변하면
    if num != beads[i]:
      #새로운 숫자 반영
      num = beads[i]
      end = i
      #end - start는 구슬그룹에 속한 구슬 개수
      changed_beads.append(end-start)
      #beads[start]는 해당 구슬 그룹의 구슬번호
      changed_beads.append(beads[start])
      #새로운 구슬 그룹의 시작 인덱스 start
      start = i
  #변화가 완료된 구슬길이가 N*N-1이 되도록 0을 채워줌
  if len(changed_beads) < N*N-1:
    for _ in range(N*N-1 - len(changed_beads)):
      changed_beads.append(0)
  #길이가 N*N-1이 넘으면 넘친구슬은 버림
  beads = changed_beads[:N*N-1]  
  #구슬의 변화를 grid에 반영
  for i in range(N*N-1):
        row, col = grid_indexing[i]
        grid[row][col] = beads[i]
  return
#상 하 좌 우
direction = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
magic = [list(map(int,input().split())) for _ in range(M)]
grid_indexing = []
shark_r = N//2
shark_c = N//2
beads = []
explosed_beads = [0,0,0]
result = 0
for distance in range(1, N + 1):
  if distance % 2:
    move(distance, 0, -1)
    move(distance, 1, 0)
  else:
    move(distance, 0, 1)
    move(distance, -1, 0)

for m in range(M):
  #블리자드 구슬 파괴
  blizzard(N//2,N//2,magic[m][0], magic[m][1])
  #구슬 움직임
  beadsMove()
  #구슬 폭발 & 이동
  while True:
    if not explosion():
      break
    beadsMove()
  #구슬 변화
  beadsChange()
for i in range(3):
  result += explosed_beads[i] * (i + 1)
print(result)