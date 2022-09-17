#국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면,
#두 나라가 공유하는 국경선을 오늘 하루동안 연다
#위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작.
#국경선이 열려잇어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를
#오늘 하루동안은 연합이라고 한다.
#연합을 이루고 있는 각 칸의 인구수 = 연합의 인구수 / 연합을 이루고 있는 칸의 개수
#연합을 해체하고 모든 국경선을 닫는다.
#N(배열 크기),L(이상),R(이하)
#각 국가 인구 차이 계산해서 조건 부합 확인
def bfs(row, col):
  queue = list()
  queue.append([row,col])
  #현재 국가 연합에 추가
  visited[row][col] = True
  allies = [[row,col]]
  #연합국 인구 수
  population = matrix[row][col]
  while queue:
    x, y = queue.pop(0)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #인덱스 허용범위, 방문여부 확인
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        #인구수 차이 조건
        if L <= abs(matrix[nx][ny] - matrix[x][y]) <= R:
          #연합국에 추가
          allies.append([nx,ny])
          visited[nx][ny] = True
          queue.append([nx,ny])
          #연합국 인구수에 추가
          population += matrix[nx][ny]
  #모든 연합이 끝나면 연합국들의 인구수 평균 계산 후 저장        
  for row, col in allies:
    matrix[row][col] = population // len(allies)
  #연합국 수 리턴
  return len(allies)

dx = [1,-1,0,0] # 우 좌 하 상
dy = [0,0,1,-1]
N,L,R = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = 0
#인구 이동이 없을때 까지 반복
while True:
  #모든 연합 해제
  visited = [[False] * N for _ in range(N)]
  flag = False
  for i in range(N):
    for j in range(N):
      #이미 연합된 국가 방문 안함
      if not visited[i][j]:
        #연합된 국가 수가 2이상.(자기국가 1 + 타국 @)
        if bfs(i,j) > 1:
          flag = True
  if not flag:
    break
  #인구 이동 1회
  result += 1
print(result)