N = int(input())
K = int(input())
apple_pos = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
#우, 하, 좌, 상
dir = [[0,1], [1,0], [0,-1], [-1,0]]
snake = [[0,0]]
board = [[0] * N for _ in range(N)]
board[0][0] = 1
snake_dir, time = 0, 1
dir_change = [input().split() for _ in range(L)]
# 0: 빈칸, 1: 뱀, 2: 사과
for apple in apple_pos:
  row, col = apple
  board[row - 1][col - 1] = 2 

while True:
  #뱀 머리 위치
  row, col = snake[-1]
  drow, dcol = dir[snake_dir]
  #머리가 될 위치
  nrow, ncol = row + drow, col + dcol
  #벽에 부딪히거나 뱀 몸에 부딪히면 Game Over
  if (not 0 <= nrow < N) or (not 0 <= ncol < N) or (board[nrow][ncol] == 1):
    break
  #이동하는 칸에 사과가 있으면
  if board[nrow][ncol] == 2:
    #머리 이동. 사과가 사라지고 꼬리는 움직이지 않는다.
    snake.append([nrow, ncol])
    board[nrow][ncol] = 1
  else: #이동하는 칸에 사과가 없다면,
    #머리 이동, 꼬리 삭제
    snake.append([nrow, ncol])
    board[nrow][ncol] = 1
    tail_row, tail_col = snake.pop(0)
    board[tail_row][tail_col] = 0
  for change in dir_change:
    #시간에 맞는 방향 전환
    if time == int(change[0]):
      if change[1] == "L":
        snake_dir = (snake_dir - 1) % 4
      else: snake_dir = (snake_dir + 1) % 4
      break
  time += 1
print(time)