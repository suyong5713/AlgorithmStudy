def move():
  global fire_ball, grid
  for i in range(len(fire_ball)):
    fb = fire_ball[i]
    r, c, m, s, d = fb
    dr, dc = dir[d]
    nr, nc = r + (dr*s), c + (dc*s)
    #행과 열이 순환구조
    r, c = nr % N, nc % N
    fire_ball[i] = [r, c, m, s, d]
    grid[r][c].append(fire_ball[i])
  
  return
def divide():
  global grid, fire_ball
  for i in range(N):
    for j in range(N):
      if len(grid[i][j]) > 1:
        #같은칸에 파이어볼이 두개이상이면 분열
        sum_m, sum_s = 0, 0
        d_list = []
        for k in range(len(grid[i][j])):
          sum_m += grid[i][j][k][2]
          sum_s += grid[i][j][k][3]
          d_list.append(grid[i][j][k][4])
        new_m = sum_m // 5
        if new_m == 0:
          index = 0
          while(index < len(fire_ball)):
            if fire_ball[index][:2] == [i,j]:
              fire_ball.pop(index)
            else: index += 1
          continue
        new_s = sum_s // len(grid[i][j])
        odd_cout = 0
        for d in d_list:
          if d % 2 == 1:
            odd_cout += 1
        new_fb_list = []
        if odd_cout == 0 or odd_cout == len(d_list):
          for x in range(0, 8, 2):
            new_fb_list.append([i, j, new_m, new_s, x])
        else:
          for x in range(1, 8, 2):
            new_fb_list.append([i, j, new_m, new_s, x])
        index = 0
        while(index < len(fire_ball)):
          if fire_ball[index][:2] == [i,j]:
            fire_ball.pop(index)
          else: index += 1
        fire_ball.extend(new_fb_list)

N, M, K = list(map(int,input().split()))
fire_ball = []
  
for _ in range(M): 
  #r, c, m(질량), s(속도), d(방향)
  fb = list(map(int,input().split()))
  fb[0] -= 1
  fb[1] -= 1
  fire_ball.append(fb)

dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(K):
  grid = [[[] for _ in range(N)] for _ in range(N)]
  move()
  divide()
result = 0
for fb in fire_ball:
  result += fb[2]
print(result)