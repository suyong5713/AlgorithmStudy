import sys
sys.stdin = open("input.txt", "r")

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    r, c = map(int, input().split())
    apples.append([r - 1, c - 1])
l = int(input())    # 뱀의 방향 변환 횟수
# 초, 방향 (L : 왼쪽, D : 오른쪽)
infos = [list(input().split()) for _ in range(l)]
# 뱀의 위치
s_x, s_y = 0, 0
# 뱀이 차지하고 있는 좌표
s_pos = []
# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0
time = 0

while True:
    # 자기 몸과 부딪히면 break
    if [s_x, s_y] in s_pos:
        break
    # 범위를 벗어나면 break
    if not 0 <= s_x < n or not 0 <= s_y < n:
        break
    # 초기 뱀의 위치 추가
    if not s_pos:
        s_pos.append([0, 0])
    s_pos.append([s_x, s_y])
    for i in infos:
        # 명령에 대한 시간에 대해
        if str(time) == i[0]:
            # "D" : 오른쪽으로 90도 회전
            if i[1] == "D":
                dir += 1
            # "L" : 왼쪽으로 90도 회전
            elif i[1] == "L":
                dir -= 1
    # 방향 범위를 벗어날 경우 조정
    if dir == 4:
        dir = 0
    elif dir == -1:
        dir = 3
    s_x += dx[dir]
    s_y += dy[dir]
    time += 1
    # 이동한 칸에 사과가 있을 경우
    if [s_x, s_y] in apples:
        # 사과만 삭제
        apples.remove([s_x, s_y])
    # 사과가 없을 경우
    else:
        # 뱀의 꼬리 삭제
        s_pos.remove(s_pos[0])

print(time)
