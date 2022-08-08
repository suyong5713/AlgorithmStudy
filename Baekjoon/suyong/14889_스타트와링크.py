def dfs(depth, index):
  global absMin
  if depth == N//2:
    #스타트팀과 링크팀 점수 초기화
    startS, linkS = 0,0
    for i in range(N):
      for j in range(N):
        #visited = true이면 strat팀. false이면 link팀
        if visited[i] and visited[j]:
          startS += S[i][j]
        elif visited[i] == False and visited[j] == False:
          linkS += S[i][j]
    #최솟값 저장
    absMin = min(absMin, abs(startS - linkS))
    return
  
  for i in range(index, N):
    if not visited[i]:
      #현재 선수보다 번호가 낮은 경우는 dfs 생략. (왔던길을 되돌아가지 말자)
      if index >= i:
        continue
      #i번째 선수를 팀으로 선택 후 dfs
      visited[i] = True
      dfs(depth+1, i)
      #i번째 선수를 팀으로 선택하지 않고 다음 dfs로 넘어가기 위해 False로 돌려놓음
      visited[i] = False
      
N = int(input())
S = []
absMin = 10**10
for i in range(N):
  S.append(list(map(int,input().split())))
visited = [False] * N
dfs(0,0)
print(absMin)
