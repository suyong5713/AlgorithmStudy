def difussion():
  temp_room = [[0] * C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      #미세먼지가 있으면
      if room[i][j] > 0:
        #4방향 확산
        dust = 0
        for dir in range(4):
          n_row = i + d_row[dir]
          n_col = j + d_col[dir]
          #공간, 공기청정기 위치 체크
          if 0 <= n_row < R and 0 <= n_col < C and room[n_row][n_col] != -1:
            temp_room[n_row][n_col] += room[i][j] // 5
            dust += room[i][j] // 5
        room[i][j] -= dust
  for i in range(R):
    for j in range(C):
      room[i][j] += temp_room[i][j]
  return

def purification():
  #위쪽 정화. 우->상->좌->하
  aircleaner_top = aircleaner[0]
  before_air = 0
  n_row = aircleaner_top[0]
  n_col = aircleaner_top[1]
  for dir in range(4):
    temp_air = 0
    while True:
      n_row += upside_row[dir]
      n_col += upside_col[dir]
      if n_row == aircleaner_top[0] and n_col == aircleaner_top[1]: break
      if 0 <= n_row < R and 0 <= n_col < C:
        temp_air = room[n_row][n_col]
        room[n_row][n_col] = before_air
        before_air = temp_air
      else:
        n_row -= upside_row[dir]
        n_col -= upside_col[dir]
        break

  #아래쪽 정화. 우->하->좌->상
  aircleaner_bottom = aircleaner[1]
  before_air = 0
  n_row = aircleaner_bottom[0]
  n_col = aircleaner_bottom[1]
  for dir in range(4):
    temp_air = 0
    while True:
      n_row += downside_row[dir]
      n_col += downside_col[dir]
      if n_row == aircleaner_bottom[0] and n_col == aircleaner_bottom[1]: break
      if 0 <= n_row < R and 0 <= n_col < C:
        temp_air = room[n_row][n_col]
        room[n_row][n_col] = before_air
        before_air = temp_air
      else:
        n_row -= downside_row[dir]
        n_col -= downside_col[dir]
        break
  return
d_row = [-1,1,0,0] #상,하,좌,우
d_col = [0,0,-1,1]  
upside_row = [0,-1,0,1] #우, 상, 좌, 하
upside_col = [1,0,-1,0]
downside_row = [0,1,0,-1]
downside_col = [1,0,-1,0]
R,C,T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
aircleaner = []
for i in range(R):
  if room[i][0] == -1:
    aircleaner.append([i,0])
    aircleaner.append([i+1,0])
    break
for t in range(T):
  difussion()
  purification()
result = 0
for i in range(R):
  for j in range(C):
    if room[i][j] > 0:
      result += room[i][j]
print(result)