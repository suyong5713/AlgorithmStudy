def attack(castle):
  #deepCopy
  copy_castle = []
  for row in castle:
    copy_castle.append(row[:])
  killCnt = 0
  for _ in range(N):
    killed = [(-1,-1)]*3
    for k in range(3):
      #궁수 1명 선정
      row, col = archer[k]
      #row,col,거리
      minDist = (0,0,N+M)
      #아래행부터 위로 탐색
      for i in range(N-1, -1, -1):
        for j in range(M):
          # 적이 사거리 내에 존재한다면
          if copy_castle[i][j] == 1 and abs(row-i) + abs(col-j) <= D:
            dist = abs(row-i) + abs(col-j)
            #최소사거리인 경우
            if dist < minDist[2]:
              minDist = (i,j,dist)
              killed[k] = (i,j)
            #최소사거리와 같은 경우 왼쪽 적 우선
            elif dist == minDist[2]:
              if minDist[1] >= j:
                minDist = (i,j,dist)
                killed[k] = (i,j)
    killed = list(set(killed))
    #죽은 적 0으로 교체
    for pos in killed:
      row,col = pos
      if row == -1: continue
      copy_castle[row][col] = 0
    #몹 배치 변경
    copy_castle.pop()
    copy_castle.insert(0,[0]*M)
    #초기값 (-1,-1)은 궁수가 적을 못죽인 경우
    killCnt += len(killed) - killed.count((-1,-1))
  return killCnt

N,M,D = map(int,input().split())
castle = [list(map(int,input().split())) for _ in range(N)]
archer = [0] * 3
maxKill = float("-inf")

for i in range(M-2):
  for j in range(i+1,M-1):
    for k in range(j+1,M):
      archer[0],archer[1],archer[2] = (N,i),(N,j),(N,k)
      maxKill = max(maxKill,attack(castle))
print(maxKill)