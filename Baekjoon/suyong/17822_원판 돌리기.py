def remove():
  delete_list = []
  for i in range(1,N+1):
    for j in range(M):
      flag = False
      #인접 4방향 탐색해서 같은 수 제거
      for k in range(4):
        drow, dcol = direction[k]
        nrow, ncol = i + drow, (j + dcol) % M
        if circle_board[nrow][ncol] == circle_board[i][j] and circle_board[i][j]:
          #인접 4방에서 i,j수와 같은 수가 있다면 flag True
          flag = True
          #삭제할 수의 위치를 담아두었다가 나중에 한번에 삭제
          delete_list.append([nrow,ncol])
      #인접 4방에서 같은 수를 찾았을 때 i,j수도 삭제
      if flag:
        delete_list.append([i,j])
  for pos in delete_list:
    row, col = pos
    circle_board[row][col] = 0
  return len(delete_list)
#원판 지름 N, 원판에 적힌 수의 개수 M, 회전 횟수 T 
N,M,T = list(map(int,input().split()))
circle_board = [list(map(int,input().split())) for _ in range(N)]
circle_board.insert(0, [0] * M)
circle_board.append([0] * M)
direction = [[0, 1],[0, -1], [1, 0], [-1, 0]]
spin_list = [list(map(int,input().split())) for _ in range(T)]
for t in range(T):
  x, d, k = spin_list[t]
  for i in range(1, N+1):
    if i >= x and i % x == 0:
      if d == 0:
        #시계방향 회전
        for _ in range(k):
          circle_board[i].insert(0, circle_board[i].pop())
      else:
        #반시계방향 회전
        for _ in range(k):
          circle_board[i].append(circle_board[i].pop(0))
  if not remove():
    #삭제할 인접 수가 없는 경우
    count, summary = 0, 0
    for row in range(1, N + 1):
      for col in range(M):
        if circle_board[row][col]:
          count += 1
          summary += circle_board[row][col]
    #원판 위에 수가 있어야 함
    if count:
      avg = summary / count
      for row in range(1, N+1):
        for col in range(M):
          if circle_board[row][col]:
            #수가 평균보다 작으면 +1, 크면 -1
            if circle_board[row][col] > avg:
              circle_board[row][col] -= 1
            elif circle_board[row][col] < avg:
              circle_board[row][col] += 1
    #원판 위에 더이상 수가 없다면 멈춤.
    else: break
result = 0
for row in circle_board:
  result += sum(row)
print(result)