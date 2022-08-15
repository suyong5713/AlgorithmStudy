def findSquare(x,y):
  row, col = 0,0
  while matrix[x+row][y]: 
    row += 1
    if x+row == N: break
  while matrix[x][y+col]: 
    col += 1
    if y+col == N: break
  
  for i in range(row):
    for j in range(col):
      matrix[x+i][y+j] = 0
  return (row,col,row*col)

def takeArea(elem):
  return elem[2]

testCase = int(input())
for tc in range(testCase):
  N = int(input())
  matrix = [list(map(int,input().split())) for _ in range(N)]
  squareList = []
  for i in range(N):
    for j in range(N):
      if matrix[i][j]:
        squareList.append(findSquare(i,j))
  squareList.sort(key=takeArea)
  for i in range(len(squareList)-1):
    if squareList[i][2] == squareList[i+1][2]:
      if squareList[i+1][0] < squareList[i][0]:
        temp = squareList[i]
        squareList[i] = squareList[i+1]
        squareList[i+1] = temp
  print("#" + str(tc+1) + " " + str(len(squareList)),end=' ')
  for i in squareList:
    print(str(i[0]) + " " + str(i[1]),end=' ')
  print()