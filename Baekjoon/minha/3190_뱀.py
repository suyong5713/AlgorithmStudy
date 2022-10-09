from collections import deque

def game():
    global answer, snake_dir, hy, hx

    while True:
        # 뱀이 현재 방향으로 몸 길이를 늘려 머리를 다음 칸에 위치 시킴
        hy += dy[snake_dir]
        hx += dx[snake_dir]

        # 머리칸이 벽 또는 자신의 몸과 부딪히면 반복문 탈출
        if not(0 <= hy < N and 0 <= hx < N) or graph[hy][hx] == 1:
            break

        # 머리칸이 사과가 없는 칸이라면, 뱀의 위치 큐에 머리 값을 넣고, 정사각 보드의 값도 1로 변경
        # 몸길이 줄여서 꼬리가 위치한 칸을 비워줌
        if graph[hy][hx] == 0:
            snake.append((hy, hx))
            graph[hy][hx] = 1
            ty, tx = snake.popleft()
            graph[ty][tx] = 0
        # 머리칸이 사과가 있는 칸이라면, 뱀의 위치 큐에 머리 값을 넣고, 정사각 보드의 값도 1로 변경
        elif graph[hy][hx] == 2:
            snake.append((hy, hx))
            graph[hy][hx] = 1

        # 현재 시간이 방향 변환 시간에 포함된다면
        if answer in change.keys():
            # 현재 시간에 바뀌어야 하는 방향이 왼쪽이면(반시계 방향) 현재 방향-1을 4로 나눈 나머지가 새로운 방향값
            if change[answer] == 'L':
                snake_dir = (snake_dir - 1) % 4
            # 현재 시간에 바뀌어야 하는 방향이 오른쪽이면(시계 방향) 현재 방향+1을 4로 나눈 나머지가 새로운 방향값
            elif change[answer] == 'D':
                snake_dir = (snake_dir + 1) % 4

        # 1초 증가
        answer += 1

# 정사각 보드 크기 N 입력 받고, 정사각 보드 0으로 초기화
N = int(input())
graph = [[0] * N for _ in range(N)]

# 사과의 개수와 위치 입력 받고, 정사각 보드에 사과가 있는 위치값 2로 바꾸기
K = int(input())
for _ in range(K):
    R, C = map(int, input().split())
    graph[R - 1][C - 1] = 2

# 방향 전환 횟수와 방향 정보 입력 받고, key : 시간, value : 방향인 딕셔너리에 정보 저장
L = int(input())
change = dict()
for _ in range(L):
    X, C = input().split()
    change[int(X)] = C

# 오른쪽 향하는 것이 index 0, 시계 방향(오른쪽)으로
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 처음 뱀의 머리 위치 0, 0와 방향 0
hy, hx = 0, 0
snake_dir = 0
# 뱀의 위치 넣을 큐에 처음 머리 위치 넣고, 정사각 보드의 값도 1로 바꾸기
snake = deque()
snake.append((hy, hx))
graph[hy][hx] = 1

answer = 1
game()
print(answer)