import copy
from collections import deque

# 원판 돌리기
def rotate(x, d, k):
    global stencil, n
    # x의 배수인 원판 찾기
    targets = []
    for i in range(1, n + 1):
        if i % x == 0:
            targets.append(i - 1)
    for target in targets:
        for _ in range(k):
            # 시계 방향
            if d == 0:
                stencil[target].rotate(1)
            # 반시계 방향
            else:
                stencil[target].rotate(-1)

# 같은 숫자 삭제
def remove():
    global stencil
    temp = copy.deepcopy(stencil)
    # 한 원판에 대한 숫자 삭제
    for i in range(n):
        for j in range(m):
            if stencil[i][j] == -1: continue
            if stencil[i][(j - 1 + m) % m] == stencil[i][j]:
                temp[i][j] = 0
                temp[i][(j - 1 + m) % m] = 0
            if stencil[i][(j + 1 + m) % m] == stencil[i][j]:
                temp[i][j] = 0
                temp[i][(j + 1 + m) % m] = 0
    # 원판끼리 같은 숫자 검색 후 삭제
    for j in range(m):
        for i in range(1, n):
            if stencil[i][j] == 0: continue
            if stencil[i - 1][j] == stencil[i][j]:
                temp[i][j] = 0
                temp[i - 1][j] = 0
    # 삭제한 수가 없을 경우 false를 반환하여 평균 관련 함수로 이동
    if stencil == temp:
        return False
    stencil = temp
    return True

# 인접한 수 중 같은 수가 없을 경우 평균에 대해 원판 숫자 변경
def change_avg():
    # 값이 0이 아닌 칸들에 대한 좌표
    num_list = []
    # 값이 0이 아닌 칸들의 합
    sum_num = 0
    for i in range(n):
        for j in range(m):
            if stencil[i][j] > 0:
                num_list.append((i, j))
                sum_num += stencil[i][j]
    if sum_num != 0:
        aver = sum_num / len(num_list)
    for (x, y) in num_list:
        if stencil[x][y] > aver:
            stencil[x][y] -= 1
        elif stencil[x][y] < aver:
            stencil[x][y] += 1


# 원판 크기, 각 원판의 정수 개수, 회전 횟수
n, m, t = map(int, input().split())
# 원판
stencil = [deque(list(map(int, input().split()))) for _ in range(n)]
# x의 배수, 방향, 칸 수
for i in range(t):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    if not remove():
        change_avg()
result = 0
for i in range(n):
    for j in range(m):
        result += stencil[i][j]

print(result)