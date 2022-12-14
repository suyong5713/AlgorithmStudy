import copy

def solve(shark_row, shark_col, eat_sum, room):
  global result 
  #상어 위치의 물고기가 먹히고 0으로 변경.
  eat_sum += room[shark_row][shark_col][0]
  room[shark_row][shark_col][0] = 0
  #물고기의 방향을 상어가 획득
  shark_dir = room[shark_row][shark_col][1]
  result = max(result, eat_sum)

  #작은 물고기부터 이동 1~16
  for fish in range(1,17):
    fish_pos = []
    for i in range(4):
      for j in range(4):
        if fish == room[i][j][0]:
          fish_pos = [i,j]

    #물고기가 이미 먹히고 없음
    if not fish_pos:
      continue

    fish_row, fish_col = fish_pos
    fish_dir = room[fish_row][fish_col][1]
    #반시계 회전
    for i in range(8):
      direction = (fish_dir + i) % 8
      fish_drow, fish_dcol = dir[direction]
      fish_nrow, fish_ncol = fish_row + fish_drow, fish_col + fish_dcol
      #이동할 곳이 범위 내 이면서 상어 위치와 달라야 함.
      if 0 <= fish_nrow < 4 and 0 <= fish_ncol < 4 and not ((fish_nrow,fish_ncol) == (shark_row, shark_col)):
        #반시계 회전으로 변경된 물고기의 이동방향 갱신
        room[fish_row][fish_col][1] = direction
        #물고기와 위치 변경
        room[fish_row][fish_col], room[fish_nrow][fish_ncol] = room[fish_nrow][fish_ncol], room[fish_row][fish_col]
        break

  #공간 크기가 4 X 4이므로 상어 최대 이동거리는 4
  for dist in range(1, 4):
    shark_drow, shark_dcol = dir[shark_dir]
    #주어진 이동방향으로 1~4만큼 이동했을 때의 위치
    shark_nrow, shark_ncol = shark_row + (dist * shark_drow), shark_col + (dist * shark_dcol)
    #이동할 위치가 범위 내 이면서 물고기가 있어야 함
    if 0 <= shark_nrow < 4 and 0 <= shark_ncol < 4 and room[shark_nrow][shark_ncol][0] > 0:
      solve(shark_nrow, shark_ncol, eat_sum, copy.deepcopy(room))
  return

#↑, ↖, ←, ↙, ↓, ↘, →, ↗
dir = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
fish_info = [list(map(int,input().split())) for _ in range(4)]
room = []
result = 0
for i in range(4):
  row = []
  for j in range(0, 8, 2):
      row.append([fish_info[i][j], fish_info[i][j+1]-1])
  room.append(row)
solve(0, 0, 0, room)
print(result)