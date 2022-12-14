def solve(row,col,d1,d2):
  global town

  #5구역 경계선 설정
  section = [[0] * (N + 1) for _ in range(N+1)]
  for i in range(0, d1 + 1):
    #1
    section[row + i][col - i] = 5
    #4
    section[row+d2 + i][col+d2 - i] = 5
  for i in range(0, d2 + 1):
    #2
    section[row + i][col + i] = 5
    #3
    section[row+d1 + i][col-d1 + i] = 5

  population = [0,0,0,0,0]
  total_population = 0
  for t in town:
    total_population += sum(t)
  # 1구역
  for i in range(1, row+d1):
    for j in range(1, col + 1):
      if section[i][j] == 5:
        break
      else:
        population[0] += town[i - 1][j - 1]
        section[i][j] = 1
  # 2구역
  for i in range(1,row + d2 + 1):
    for j in range(N, col, -1):
      if section[i][j] == 5:
        break
      else:
        population[1] += town[i - 1][j - 1]
        section[i][j] = 2
  # 3구역
  for i in range(row + d1, N+1):
    for j in range(1, col - d1 + d2):
      if section[i][j] == 5:
        break
      else:
        population[2] += town[i - 1][j - 1]
        section[i][j] = 3
  # 4구역
  for i in range(row + d2 + 1, N + 1):
    for j in range(N, col - d1 + d2 - 1, -1):
      if section[i][j] == 5:
        break
      else:
        population[3] += town[i - 1][j - 1]
        section[i][j] = 4
  population[4] = total_population - sum(population[0:4])
  return max(population) - min(population)
N = int(input())
town = [list(map(int,input().split())) for _ in range(N)]
section = [[0] * N for _ in range(N)]

# solve(3,3,1,1)
min_value = float("inf")
for row in range(1,N + 1):
  for col in range(1,N + 1):
    for d1 in range(1,N + 1):
      for d2 in range(1,N + 1):
        if row + d1 + d2 > N:
          continue
        if col - d1 < 1:
          continue
        if col + d2 > N:
          continue
        min_value = min(min_value,solve(row,col,d1,d2))
print(min_value)