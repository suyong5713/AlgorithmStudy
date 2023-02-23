# https://www.acmicpc.net/problem/15686
# 치킨 배달, 브루트포스/DFS

from collections import deque
import sys

def dfs(cnt, idx):
    global n, m, min_distance

    if cnt == m:
        distance = 0

        for i, j in homes:
            min_chicken_distance = sys.maxsize

            for cy, cx in stack:
                # 집(i, j)과 치킨집(cy, cx) 사이의 거리 계산
                chicken_distance = abs(i - cy) + abs(j - cx)
                min_chicken_distance = min(min_chicken_distance, chicken_distance)
            
            distance += min_chicken_distance
        
        # 치킨 거리의 최소값 갱신
        min_distance = min(min_distance, distance)

        return
    
    for i in range(idx, len(chickens)):
        stack.append(chickens[i])
        dfs(cnt + 1, i + 1)
        stack.pop()

# N : N×N 크기의 도시
# M : 치킨집 M개 고르기
n, m = map(int, input().split())

# 0 : 빈 칸
# 1 : 집
# 2 : 치킨집
board = [list(map(int, input().split())) for _ in range(n)]

homes = []    # 집의 위치
chickens = [] # 치킨집의 위치

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

# 최소 치킨 거리
min_distance = sys.maxsize

# 스택을 사용하기 위해 deque 선언
stack = deque()

dfs(0, 0)

print(min_distance)
