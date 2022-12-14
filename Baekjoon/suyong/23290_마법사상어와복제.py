from copy import copy
import itertools
import copy
fish_dx = [-1,-1,0,1,1,1,0,-1]
fish_dy = [0,-1,-1,-1,0,1,1,1]
shark_dx = [0,-1,0,1] #상 좌 하 우
shark_dy = [-1,0,1,0]
M,S = map(int,input().split())
#물고기 좌표와 방향정보
fish_info = [list(map(int,input().split())) for _ in range(M)]
smell = []
smell_life = []
#상어 좌표
shark = list(map(int,input().split()))
shark_move = list(map(list,itertools.combinations_with_replacement([1,2,3,4], 3)))
#물고기 방향 인덱스와 통일
for j in range(M): fish_info[j][2] -= 1
for i in range(S):
  if len(smell_life) > 0:
    try:
      for i in range(len(smell_life)):
        smell_life[i] -= 1
        if smell_life[i] == 0:
          smell_life.pop(i)
          smell.pop(i)
    except:pass

  temp_fish_info = copy.deepcopy(fish_info)
  #물고기 이동
  for idx,fish in enumerate(temp_fish_info):
    row, col, direction = fish
    #다음 이동할 공간. 상어있으면 안됨. 격자밖으로 나가면 안됨. 물고기냄새나면 안됨.
    for j in range(8):
      next_col = col + fish_dx[direction]
      next_row = row + fish_dy[direction]
      if 1 <= next_col <= 4 and 1 <= next_row <= 4 and [next_row,next_col] != shark and smell.count([next_row,next_col]) == 0:
        temp_fish_info[idx] = next_row,next_col,direction
        break
      else:
        direction = (direction - 1) % 8
  max_kill = float("-inf")
  max_kill_move = "999"
  for move in shark_move:
    move_str = ""
    kill_count = 0
    visited = [[False] * 4 for _ in range(4)]
    shark_row, shark_col = shark[:]
    visited[shark_row-1][shark_col-1] = True
    for dir in move:
      move_str += str(dir)
      next_col = shark_col + shark_dx[dir - 1]
      next_row = shark_row + shark_dy[dir - 1]
      if 1 <= next_col <= 4 and 1 <= next_row <= 4 and not visited[next_row-1][next_col-1]:
        visited[next_row-1][next_col-1] = True
        shark_row,shark_col =  next_row,next_col
        for j in range(len(temp_fish_info)):
          if list(temp_fish_info[j][:2]) == [shark_row, shark_col]:
            kill_count += 1
      else:
        break
    if int(move_str) < 100:
      continue
    if max_kill < kill_count:
      max_kill = kill_count
      max_kill_move = move_str
    #사전 순
    elif max_kill == kill_count and int(max_kill_move) > int(move_str):
      max_kill_move = move_str
  for dir in max_kill_move:
    next_row = shark[0] + shark_dy[int(dir) - 1]
    next_col = shark[1] + shark_dx[int(dir) - 1]
    shark = next_row,next_col
    j = 0
    while j != len(temp_fish_info):
      if list(temp_fish_info[j][:2]) == [next_row,next_col]:
        smell.append(list(temp_fish_info.pop(j)[:2]))
        smell_life.append(3)
        j -= 1
      j+=1
  for temp_fish in temp_fish_info:
    fish_info.append(temp_fish)
print(len(fish_info))