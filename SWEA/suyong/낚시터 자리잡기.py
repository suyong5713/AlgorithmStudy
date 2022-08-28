#순열 구하기
def dfs(arr):
  if len(arr) == 3:
    temp = []
    for i in arr:
      temp.append(loc_and_count[i])
    result.append(temp)
    return
  for i in range(3):
    if not used[i]:
      used[i] = True
      arr.append(gate[i])
      dfs(arr)
      used[i] = False
      arr.pop()

def backTracking(gate_num, gate_waiting, visited, dist):
  global min_dist
  #현재 게이트에 배치를 기다리는 사람
  if gate_waiting == 0:
    if gate_num == 3:
      #세번째 게이트에 모든 낚시꾼이 낚시터에 입장하면,
      min_dist = min(min_dist, dist)
      return
    else:
      backTracking(gate_num+1, row[gate_num][1], visited, dist)
      return
  loc, _= row[gate_num-1]
  #게이트 위치의 낚시터가 비어있으면 배치
  if not visited[loc]:
    visited[loc] = True
    backTracking(gate_num, gate_waiting - 1, visited, dist + 1)
    visited[loc] = False
  #좌우 탐색
  else:
    flag = False
    for i in range(1,area_count+1):
      #좌,우 중 하나라도 배치되면 반복문 중지
      if 0 < loc-i <= area_count:
        if not visited[loc-i]:
          visited[loc-i] = True
          backTracking(gate_num, gate_waiting -1, visited, dist + i + 1)
          visited[loc-i] = False
          flag = True
      if 0 < loc+i <= area_count:
        if not visited[loc+i]:
          visited[loc+i] = True
          backTracking(gate_num, gate_waiting - 1, visited, dist + i + 1)
          visited[loc+i] = False
          flag = True
      if flag: break
  return
testCase = int(input())
for tc in range(testCase):
  area_count = int(input())
  loc_and_count = [list(map(int,input().split())) for _ in range(3)]
  min_dist = float("inf")
  filled = [False] * (area_count+1)
  used = [False] * 3
  gate = [0,1,2]
  result = []
  dfs([])
  #result 는 3차원 배열
  #result[0]첫번째 순열로 정해진 게이트1, 2, 3
  #result[0][0]은 게이트1의 위치와 낚시꾼 수. 즉 [location, fisher_count]
  for row in result:
    #첫번째 게이트의 낚시꾼 수를 전달
    backTracking(1,row[0][1],filled[:],0)
  print("#{} {}".format(tc+1,min_dist))

