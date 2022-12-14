n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0] #좌, 하, 우, 상
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
  flag = 0
  #4방향 탐색
  for _ in range(4):
    # 0 3 2 1
    nx = r + dx[(d+3) % 4]
    ny = c + dy[(d+3) % 4]
    # 한번 돌았으면 그 방향으로 작업시작
    d = (d+3) % 4
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        r = nx
        c = ny
        #청소 여부 확인
        flag = 1
        break
  #모든 방향이 청소되었으면
  if flag == 0:
    #후진한 위치가 벽일때
    if graph[r-dx[d]][c-dy[d]] == 1:
      print(cnt)
      break
    else:
      #후진
      r,c = r-dx[d], c-dy[d]