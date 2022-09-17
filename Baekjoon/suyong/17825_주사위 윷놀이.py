def backTracking(depth, sum_score, unit):
  global result
  if depth == 10:
    result = max(sum_score, result)
    return
  for i in range(4):
    pos = unit[i]
    #파란색 갈림길 설정
    next_pos = graph[pos][-1]
    #위 next_pos을 1칸 이동했다고 인정. 따라서 주사위 눈 - 1칸 이동
    for _ in range(1, dice[depth]):
      #한번 이동 시작하면 무조건 빨간색 화살표
      next_pos = graph[next_pos][0]
      #도착지점에서 멈춤
      if next_pos == 32:
        break
    #이동 조건 체크
    #다른 말의 위치가 도착지점이면 겹치기 상관없음
    #다른 말의 위치가 도착지점이 아니면 겹치면 안됨.
    if next_pos == 32 or (next_pos < 32 and next_pos not in unit):
        #이동전 위치 기록
        temp_pos = unit[i]
        unit[i] = next_pos
        backTracking(depth+1, sum_score + score[next_pos], unit)
        unit[i] = temp_pos
#점수값이 고유하지 않기 때문에 그래프로 사용 불가. 따라서 분리.
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], 
        [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], 
        [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13,
        16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice = list(map(int,input().split()))
result = 0
unit = [0,0,0,0]
backTracking(0, 0, unit)
print(result)
