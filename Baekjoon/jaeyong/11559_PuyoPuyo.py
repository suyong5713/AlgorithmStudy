# https://www.acmicpc.net/problem/11559
# Puyo Puyo, 구현/BFS

from collections import deque

# 탐색 범위
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 뿌요뿌요 4개 탐색
def bfs(i, j, visited, trace):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    trace.append((i, j))

    while queue:
        ny, nx = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < HEIGHT and 0 <= x < WIDTH and board[y][x] == board[i][j] and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True

                trace.append((y, x))

# 아래로 정렬
def down():
    for x in range(WIDTH):
        queue = deque()

        for y in range(HEIGHT - 1, -1, -1):
            if board[y][x] != '.':
                queue.append(board[y][x])
        
        for y in range(HEIGHT -1, -1, -1):
            if queue:
                board[y][x] = queue.popleft()
            else:
                board[y][x] = '.'

# 세로, 가로 크기 정의
HEIGHT = 12
WIDTH = 6

# 입력
board = [list(input()) for _ in range(HEIGHT)]

# 결과값
result = 0

# board 탐색
while True:
    flag = False                                        # BFS 탐색을 했는지 여부, 없으면 board 탐색 종료
    visited = [[False] * WIDTH for _ in range(HEIGHT)]  # 방문 확인
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 빈 칸이 아니면서, 방문한 적이 없던 곳인 경우
            if board[i][j] != '.' and visited[i][j] == False:
                trace = []
                bfs(i, j, visited, trace)

                # 4개 이상인지 확인 후 터트리기 및 삭제
                if len(trace) >= 4:
                    flag = True
                    
                    # BFS 탐색을 통한 경로를 따라 모두 없애기
                    for y, x in trace:
                        board[y][x] = '.'

    if flag == False:
        break
    
    # 연속으로 터트려야 하기 때문에 한 번에 중력 적용
    down()
    result += 1

print(result)
