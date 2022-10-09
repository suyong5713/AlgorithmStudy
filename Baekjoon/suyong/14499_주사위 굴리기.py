#4방향으로 주사위가 굴렀을때 전개도 변화
def rollLeft():
  dice[1].append(dice[3].pop(1))
  dice[3].insert(1, dice[1].pop(0))
def rollRight():
  dice[1].insert(0,dice[3].pop(1))
  dice[3].insert(1,dice[1].pop())
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

dice = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
N, M, x, y, K = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
dice_pos = [x,y]
# 1.동쪽, 2.서쪽 3.북쪽 4.남쪽
dir = [0,[0, 1], [0, -1], [-1,0], [1,0]]
command_list = list(map(int,input().split()))

for command in command_list:
  #범위 밖을 벗어나는 명령은 무시해야 함
  row, col = dice_pos
  drow, dcol = dir[command]
  nrow, ncol = row + drow, col + dcol
  if 0 <= nrow < N and 0 <= ncol < M:
    #명령 방향으로 구르기
    if command == 1:
      rollRight()
    elif command == 2:
      rollLeft()
    elif command == 3:
      rollUp()
    else: rollDown()
    #주사위 위치 변경
    dice_pos = [nrow, ncol]
    #칸에 있는 수 0이면 주사위 바닥면 숫자 복사
    if board[nrow][ncol] == 0:
      board[nrow][ncol] = dice[3][1]
    else:
      #칸에 있는 수가 0아니면 주사위 바닥면에 숫자 복사 후 칸 수 0.
      dice[3][1]= board[nrow][ncol]
      board[nrow][ncol] = 0
    print(dice[1][1])