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
def remove_row_or_col():
  global destroy_count, green_board, blue_board
  blue_board = list(map(list,zip(*blue_board)))
  for idx, row in enumerate(green_board):
    if row == [1]*4:
      green_board.pop(idx)
      green_board.insert(0, [0] * 4)
      destroy_count += 1
  for idx, row in enumerate(blue_board):
    if row == [1] * 4:
      blue_board.pop(idx)
      blue_board.insert(0,[0]*4)
      destroy_count += 1
  while green_board[5].count(1) > 0:
    green_board.pop()
    green_board.insert(0,[0]*4)
  while blue_board[5].count(1) > 0:
    blue_board.pop()
    blue_board.insert(0,[0]*4)
  blue_board = list(map(list,zip(*blue_board)))

block_count = int(input())
block_list = [list(map(int,input().split())) for _ in range(block_count)]
green_board = [[0] * 4 for _ in range(10)]
blue_board = [[0] * 10 for _ in range(4)]

block_count, destroy_count = 0,0
while block_list:
  block = block_list.pop(0)
  block_type, x, y = block
  moveBlueBoard(block_type, x, y)
  moveGreenBoard(block_type,x,y)
  remove_row_or_col()
for row in blue_board:
  block_count += row.count(1)
for row in green_board:
  block_count += row.count(1)

print(destroy_count)
print(block_count)