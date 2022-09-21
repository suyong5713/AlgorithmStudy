from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 인접 블록 찾기 -> 블록 크기, 무지개크기, 블록좌표 리턴
def bfs(x, y, color):
    queue = deque()
    queue.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num_block, num_rainbow = 1, 0
    blocks, rainbows = [[x, y]], []
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 범위 내에 있고 방문하지 않은 일반 블록
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == color:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                num_block += 1
                blocks.append([nx, ny])
            # 범위 내에 있고 방문하지 않은 무지개 블록
            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                num_block += 1
                num_rainbow += 1
                rainbows.append([nx, ny])

    for x, y in rainbows:
        visited[x][y] = 0

    return [num_block, num_rainbow, blocks + rainbows]

# 블록 제거
def remove(block):
    for x, y in block:
        # 어떤 블록에서도 쓰이지 않는 -2 숫자로 변경
        area[x][y] = -2

# 중력
def gravity(arr):
    # 아래에서부터 확인
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if arr[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    # 아래 칸 격자 내에 존재하며 빈칸일 경우
                    if 0 <= r + 1 < n and arr[r + 1][j] == -2:
                        # 아래 칸으로 이동 후 현재 칸 비워 줌
                        arr[r + 1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break

# 반시계방향 회전
def rotate(arr):
    # 전치시킨 후 반대로 뒤집으면 90도 반시계 회전
    rotate_arr = list(map(list, zip(*arr)))[::-1]
    return rotate_arr

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
score = 0
while True:
    visited = [[0] * n for _ in range(n)]
    # 블록 그룹들을 넣을 배열
    blocks = []
    for i in range(n):
        for j in range(n):
            if area[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, area[i][j])  # 인접한 블록 찾기
                # block_info = [블록크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 블록 그룹이 존재하지 않으면 끝
    if not blocks:
        break
    # 오토 플레이
    remove(blocks[0][2])
    score += blocks[0][0] ** 2
    gravity(area)
    area = rotate(area)
    gravity(area)

print(score)
