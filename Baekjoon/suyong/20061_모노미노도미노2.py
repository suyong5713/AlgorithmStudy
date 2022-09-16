def moveGreenBoard(block_type, x, y):
  #아래로 이동 x: 행, y: 열
  nx = x+1
  if block_type == 1:
    while 0 <= nx < 10:
      if green_board[nx][y] == 0:
        nx += 1
      else:
        break
  elif block_type == 2:
    while 0 <= nx < 10:
      if green_board[nx][y] == 0 and green_board[nx][y+1] == 0:
        nx += 1
      else:
        break
    green_board[nx-1][y+1] = 1
  elif block_type == 3:
    while 0 <= nx < 9:
      if green_board[nx][y] == 0 and green_board[nx+1][y] == 0:
        nx += 1
      else:
        break
    green_board[nx][y] = 1
  green_board[nx-1][y] = 1
  return  
def moveBlueBoard(block_type, x, y):
  #오른쪽으로 이동 x: 행, y: 열
  ny = y+1
  if block_type == 1:
    while 0 <= ny < 10:
      if blue_board[x][ny] == 0:
        ny += 1
      else:
        break
  elif block_type == 2:
    while 0 <= ny < 9:
      if blue_board[x][ny] == 0 and blue_board[x][ny+1] == 0:
        ny += 1
      else:
        break
    blue_board[x][ny] = 1
  elif block_type == 3:
    while 0 <= ny < 10:
      if blue_board[x][ny] == 0 and blue_board[x+1][ny] == 0:
        ny += 1
      else:
        break
    blue_board[x+1][ny-1] = 1
  blue_board[x][ny-1] = 1
  return
def remove_row_or_col():
  global destroy_count, green_board, blue_board
  #행렬 회전. 초록색 보드와 같은 형태로 변환
  blue_board = list(map(list,zip(*blue_board)))
  for idx, row in enumerate(green_board):
    #한 행에 블럭이 꽉 찼으면 파괴
    if row == [1]*4:
      green_board.pop(idx)
      green_board.insert(0, [0] * 4)
      destroy_count += 1
  for idx, row in enumerate(blue_board):
    if row == [1] * 4:
      blue_board.pop(idx)
      blue_board.insert(0,[0]*4)
      destroy_count += 1
  #각각의 영역에서 블럭 파괴 후에도 연한색 영역에 블럭이 남아있다면 파괴.
  while green_board[5].count(1) > 0:
    green_board.pop()
    green_board.insert(0,[0]*4)
  while blue_board[5].count(1) > 0:
    blue_board.pop()
    blue_board.insert(0,[0]*4)
  #원래대로 회전
  blue_board = list(map(list,zip(*blue_board)))
#########################################################################
block_count = int(input())
block_list = [list(map(int,input().split())) for _ in range(block_count)]
#빨간 보드를 포함하게 각각의 보드 생성
green_board = [[0] * 4 for _ in range(10)]
blue_board = [[0] * 10 for _ in range(4)]
block_count, destroy_count = 0,0
while block_list:
  block = block_list.pop(0)
  block_type, x, y = block
  moveBlueBoard(block_type, x, y)
  moveGreenBoard(block_type,x,y)
  #블록 이동 후 행 열이 채워거나
  #블럭이 넘칠 때 행 또는 열 파괴
  remove_row_or_col()
#최종 남은 블럭 개수
for row in blue_board:
  block_count += row.count(1)
for row in green_board:
  block_count += row.count(1)

print(destroy_count)
print(block_count)