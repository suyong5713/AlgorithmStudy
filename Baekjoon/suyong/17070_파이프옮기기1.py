def dfs(row,col,shape):
  global count
  if row == N-1 and col == N-1:
    count+=1
    return
  #파이프가 가로 or 대각선
  if shape == 0 or shape == 2:
    if col+1 < N and house[row][col+1] == 0:
      dfs(row, col+1, 0)
  #파이프가 세로 or 대각선
  if shape == 1 or shape == 2:
    if row+1 < N and house[row+1][col] == 0:
      dfs(row+1, col, 1)
  if shape == 0 or shape == 1 or shape == 2:
    if row+1 < N and col + 1 < N:
      #대각선으로 있는 경우 차지하는 공간 전부 체크
      if house[row+1][col+1] == 0 and house[row+1][col] == 0 and house[row][col+1] == 0:
        dfs(row+1, col+1, 2)
  return
N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
count = 0
#shape 0:가로, 1:세로, 2:대각선
dfs(0,1,0)
print(count)