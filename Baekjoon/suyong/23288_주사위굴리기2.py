#4방향으로 주사위가 굴렀을때 전개도 변화
def rollLeft():
  temp = dice[1][0]
  dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[1][1],dice[1][2],dice[3][1],temp
def rollRight():
  temp = dice[1][2]
  dice[1][2],dice[1][1],dice[1][0],dice[3][1] = dice[1][1],dice[1][0],dice[3][1],temp
def rollUp():
  temp = dice[0][1]
  for i in range(0, 3):
    dice[i][1] = dice[i+1][1]
  dice[3][1] = temp
def rollDown():
  temp = dice[3][1]
  for i in range(3,0,-1):
    dice[i][1] = dice[i-1][1]
  dice[0][1] = temp

def getScore(row, col):
  queue = [[row,col]]
  visited = [[False] * M for _ in range(N)]
  visited[row][col] = True
  #주사위가 있는 위치도 개수에 포함
  result = 1
  while queue:
    i, j = queue.pop(0)
    for k in range(4):
      d_r, d_c = direction[k]
      nr, nc = i + d_r, j + d_c
      if 0 <= nr < N and 0 <= nc < M and board[row][col] == board[nr][nc]:
        if not visited[nr][nc]:
          visited[nr][nc] = True
          queue.append([nr,nc])
          result += 1
  #획득 점수 = 같은숫자 칸의 개수 * 해당 칸의 수
  return result * board[row][col]
#북(0) 서(1) 남(2) 동(3)
direction = [[-1,0],[0,-1],[1,0],[0,1]]
#세로, 가로, 이동횟수
N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dice = [[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
row, col = 0,0
roll_dir = 3
score = 0
for _ in range(K):
  #주사위 구르기
  d_r, d_c = direction[roll_dir]
  nr, nc = row + d_r, col + d_c
  if not (0 <= nr < N and 0 <= nc < M):
    #이동 방향에 칸이 없으면 방향 반대로 전환
    roll_dir = (roll_dir + 2) % 4
    d_r, d_c = direction[roll_dir]
    nr, nc = row + d_r, col + d_c
  #설정된 방향으로 주사위가 구름
  if roll_dir == 0:
    rollUp()
  elif roll_dir == 1:
    rollLeft()
  elif roll_dir == 2:
    rollDown()
  elif roll_dir == 3:
    rollRight()
  #점수 획득
  score += getScore(nr, nc)
  #주사위 밑면 숫자
  dice_bottom = dice[3][1]
  #주사위 밑면 숫자와 해당 칸의 숫자에 따른 방향 전환
  if dice_bottom > board[nr][nc]:
    #시계방향 회전
    roll_dir = (roll_dir - 1) % 4
  elif dice_bottom < board[nr][nc]:
    #반시계방향 회전
    roll_dir = (roll_dir + 1) % 4
  row, col = nr, nc
print(score)