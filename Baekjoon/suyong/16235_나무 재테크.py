#1x1크기의 칸에 여러개의 나무가 심어져 있을 수 있다.
#나무는 사계절을 보낸다.
#봄에는 자신의 나이만큼 양분을 먹고 나이가 1증가.
#각각의 나무는 나무가 있는 1x1크기의 칸에 있는 양분만 먹을 수 있다.
#하나의 칸에 여러개의 나무가 있다면 나이가 어린 나무부터 양분을 먹는다
#만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없다면 죽는다.
#여름에는 봄에 죽은 나무가 양분으로 변화.
#죽은나무의 나이 // 2 만큼 양분 추가. 소수점 버림
#가을에는 나무가 번식. 번식하는 나무는 나이가 5배수.
#인접한 8개의 칸에 나이가 1인 나무가 생김
#겨울에는 로봇이 돌아다니며 땅에 양분 추가. 양분 양은 입력으로 주어짐
#K년 이후에 살아있는 나무의 수 구하기.
#좌측부터 시계방향. 좌하 까지

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
#N은 땅 크기
N,M,K = map(int,input().split())
A = [[5] * N for _ in range(N)]
#R번째 줄 C번째 값은 A[R][C]. 즉 1번째 줄 1번째 값은 A[1][1]
S2D2 = [list(map(int,input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  x,y, age = map(int,input().split())
  tree[x-1][y-1].append(age)
for _ in range(K):
  for i in range(N):
    for j in range(N):
      if tree[i][j]:
        #봄
        tree[i][j].sort()
        alive_tree = []
        #처음엔 죽은 나무 나이를 리스트에 저장하고 sum해서 // 2 한 값을 A배열에 저장했는데 시간초과.
        nutrient = 0
        for tree_age in tree[i][j]:
          if tree_age <= A[i][j]:
            A[i][j] -= tree_age
            alive_tree.append(tree_age + 1)
          #양분이 부족하면
          else: nutrient += tree_age // 2
        tree[i][j] = alive_tree
        #여름. 모든 양분 흡수 후 죽은나무 양분 추가
        A[i][j] += nutrient
  if not tree:
    break
  #봄 여름 과정에 나무가 번식되어 추가되면 영향을 미치므로 분리.
  for i in range(N):
    for j in range(N):
      if tree[i][j]:  
        #가을
        for tree_age in tree[i][j]:
          if tree_age % 5 == 0:
            for k in range(8):
              next_row = i + dy[k]
              next_col = j + dx[k]
              if 0 <= next_row < N and 0 <= next_col < N:
                tree[next_row][next_col].append(1)
  #겨울
  for i in range(N):
    for j in range(N):
        A[i][j] += S2D2[i][j]
result = 0
for i in range(N):
  for j in range(N):
    result += len(tree[i][j])
print(result)
