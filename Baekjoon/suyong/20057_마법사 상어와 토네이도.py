#x->y로 토네이도가 이동하면 y의 주변 좌표들에 y모래 비율만큼 분산.
# 모래 계산하는 함수
def move(dist, d_row, d_col, direction):
  global result, pos_row, pos_col
  #토네이도 이동
  for _ in range(dist):
    pos_row += d_row
    pos_col += d_col
    if pos_col < 0:
      break
    #분산된 전체 모래 양
    total = 0
    for row, col, percent in direction:
      next_row = pos_row + row
      next_col = pos_col + col
      #알파 영역
      if percent == 0:
        move_sand = sand[pos_row][pos_col] - total
      else:
        move_sand = int(sand[pos_row][pos_col] * percent)
        total += move_sand
      #인덱스 유효성 검사
      if 0 <= next_row < N and 0 <= next_col < N:
        sand[next_row][next_col] += move_sand
      #격자 밖으로 나간 모래 추가
      else:
        result += move_sand
N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
#row, col, percent
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(row, -col, percent) for row, col, percent in left]
down = [(-col, row, percent) for row, col, percent in left]
up = [(col, row, percent) for row, col, percent in left]
#이동 전 좌표
pos_row, pos_col = N//2, N//2
#격자 밖으로 나간 모래
result = 0
# 토네이도 회전 패턴. 1(좌),1(하),2(우),2(상),3(좌),3(하),4(우),4(상)...
for distance in range(1, N + 1):
  if distance % 2:
    move(distance, 0, -1, left)
    move(distance, 1, 0, down)
  else:
    move(distance, 0, 1, right)
    move(distance, -1, 0, up)
print(result)