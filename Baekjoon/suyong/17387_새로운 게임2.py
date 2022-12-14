dir = [0, [0,1], [0,-1], [-1,0], [1,0]]
N, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
horse_info = [list(map(int,input().split())) for _ in range(K)]
board_horse = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
  horse_info[i][0] -= 1
  horse_info[i][1] -= 1
for idx, horse in enumerate(horse_info):
  row, col, _ = horse
  board_horse[row][col].append(idx)
turn = 0
flag = False
while True:
  turn += 1
  #턴 1000 넘어가면 종료
  if turn >= 1000:
    print(-1)
    break
  for idx, horse in enumerate(horse_info):
    #이동하는 말 위에 얹어진 말 리스트
    top = []
    row, col, direction = horse
    drow, dcol = dir[direction]
    nrow, ncol = row + drow, col + dcol
    #파란색 or 보드 밖 -> 방향 반전
    if not(0 <= nrow < N and 0 <= ncol < N) or board[nrow][ncol] == 2:
      if direction in [1,3]:
        direction += 1
      elif direction in [2,4]:
        direction -= 1
      #반전된 방향을 반영
      horse_info[idx][2] = direction
      nrow, ncol = row + (drow * -1), col + (dcol * -1)
      #방향 바꿨는데도 파란색 or 범위 밖이면 이동 안함
      if not(0 <= nrow < N and 0 <= ncol < N) or board[nrow][ncol] == 2:
        continue
    #현재 말이 몇번째에 쌓여있는지 저장
    index = board_horse[row][col].index(idx)
    #현재 말 포함 위에있는 말 저장
    top.extend(board_horse[row][col][index:])
    if board[nrow][ncol] == 1:
      #빨간색이면 말 얹어진 말들 순서 반전
      top = list(reversed(top))
    #이동할 칸 위에 쌓아줌
    board_horse[nrow][ncol].extend(top)
    #원래 있던 칸에서 이동한 말들 제거
    board_horse[row][col] = board_horse[row][col][:index]
    #얹어져서 이동된 말들 위치 정보 갱신
    for horse in top:
      horse_info[horse][0] = nrow
      horse_info[horse][1] = ncol
    #칸에 말이 4개 이상 쌓이면 끝
    if len(board_horse[nrow][ncol]) >= 4:
      flag = True 
      break
  if flag:
    print(turn)
    break