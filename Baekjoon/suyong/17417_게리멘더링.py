def isLinked(section):
  #visited 역할
  linked = [False] * (N+1)
  q = [section[0]]
  while len(q):
    node = q.pop(0)
    linked[node] = True
    for i in graph[node]:
      #i는 node의 인접노드
      #인접노드 중 section에 해당하는 노드만 수행
      if i in section:
        if not linked[i]:
          linked[i] = True
          q.append(i)
  #section의 요소들이 전부 연결되어 있는지 확인
  for i in section:
    if not linked[i]:
      return False
  return True

#node는 현재 노드, depth는 선택한 노드 수, end는 선거구에 포함시킬 지역 개수
def dfs(node,depth,end):
  global min_value
  if depth == end:
    section1, section2 = [],[]
    sec1_pop, sec2_pop = 0,0
    for i in range(1,N+1):
      #dfs로 방문한 지역은 section1, 방문하지 않은 지역은 section2.
      #동시에 지역구 별 인구수 계산
      if visited[i]:
        section1.append(i)
        sec1_pop += population[i]
      else:
        section2.append(i)
        sec2_pop += population[i]
    # 각 섹션에 해당하는 지역은 서로 연결되어야 한다.
    if isLinked(section1) and isLinked(section2):
      min_value = min(min_value, abs(sec1_pop - sec2_pop))
    else: return
  #지역구 1~N까지 dfs & backtracking
  for i in range(node,N+1):
    if not visited[i]:
      visited[i] = True
      dfs(node+1, depth+1, end)
      visited[i] = False
    else:
      continue
  return
N = int(input())
min_value = float("inf")
population = list(map(int,input().split()))
population.insert(0,0)
graph = [list(map(int,input().split()))[1:] for _ in range(N)]
graph.insert(0,[])
visited = [False]*(N+1)
#사실상 sec1과 sec2의 구분이 없기 때문에 지역구 N개중 절반만 선택하면 
#모든 경우의 수 탐색 가능
for i in range(1, N//2 +1):
  dfs(1, 0, i)
if min_value == float("inf"):
  print(-1)
else: print(min_value)