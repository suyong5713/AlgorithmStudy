def dfs(depth, arr):
  global perm_list
  if depth == len(monster_and_home):
    perm_list.append(arr[:])
    return
  for i in range(len(monster_and_home)):
    if not visited[i]:
      if monster_and_home[i] in [-1,-2,-3,-4] and arr.count(-monster_and_home[i]) == 0:
        continue
      visited[i] = True
      arr.append(monster_and_home[i])
      dfs(depth+1, arr)
      visited[i] = False
      arr.pop()
      
testCase = int(input())
for tc in range(testCase):
  min_time = float("inf")
  N = int(input())
  matrix = [list(map(int,input().split())) for _ in range(N)]
  #몬스터와 의뢰인 위치를 저장할 dictionary
  position_dict = {}
  #몬스터와 의뢰인이 몇번까지 있는지 저장할 list
  monster_and_home = []
  for i in range(N):
    for j in range(N):
      if matrix[i][j] != 0:
        monster_and_home.append(matrix[i][j])
        #몬스터,의뢰인번호를 key, 위치를 value
        position_dict.update({matrix[i][j]: (i,j)})
  visited = [False] * len(monster_and_home)
  arr = []
  perm_list = []
  #헌터가 몬스터나 집을 방문할 순서를 순열로 생성
  dfs(0,arr)
  for row in perm_list:
    current_position = (0,0)
    time = 0
    for i in row:
      target_position = position_dict.get(i)
      # 시간 = |x1 - x2| + |y1 - y2|
      time += abs(current_position[0] - target_position[0])
      time += abs(current_position[1] - target_position[1])
      #헌터 위치 갱신
      current_position = target_position
    min_time = min(time, min_time)
  print("#{} {}".format(tc+1, min_time))