# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 아이템 줍기 (Level. 3 / BFS)
# 풀이시간 : 40분

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    cy, cx = characterY * 2, characterX * 2
    iy, ix = itemY * 2, itemX * 2

    # 1부터 50 이하까지니까 2배, 100까지 하려면 101 
    board = [[0] * 101 for _ in range(101)]

    queue = deque()
    visited = [[False] * 101 for _ in range(101)]

    # 초기값으로 캐릭터 위치 지정
    queue.append((cy, cx, 0))
    visited[cy][cx] = True

    # 꽉 채워서 직사각형 그리기
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 * 2, y2 * 2 + 1):
            for j in range(x1 * 2, x2 * 2 + 1):
                # if y1 * 2 + 1 <= i < y2 * 2 and x1 * 2 + 1 <= j < x2 * 2: continue
                board[i][j] = True

    # 안쪽 영역 삭제, 테두리만 남기기
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 * 2 + 1, y2 * 2):
            for j in range(x1 * 2 + 1, x2 * 2):
                board[i][j] = False

    # BFS 탐색 시작
    while queue:
        ny, nx, nt = queue.popleft()

        # 아이템 위치에 캐릭터가 최단거리에 도착한 경우
        if ny == iy and nx == ix:
            return nt // 2

        # 시계방향으로 네 방향 탐색 (북, 동, 남, 서)
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < 101 and 0 <= x < 101 and board[y][x] == True and visited[y][x] == False:
                queue.append((y, x, nt + 1))
                visited[y][x] = True

    return 0

# ============================================================= #

def main(t, rectangle, characterX, characterY, itemX, itemY, result):
    r = solution(rectangle, characterX, characterY, itemX, itemY)
    print('#{}: {}, {}, {}'.format(t + 1, result == r, result, r))

if __name__ == '__main__':
    rectangle = [
      [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 
      [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 
      [[1, 1, 5, 7]], 
      [[2, 1, 7, 5], [6, 4, 10, 10]], 
      [[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]]
    ]
    characterX = [1, 9, 1, 3, 1]
    characterY = [3, 7, 1, 1, 4]
    itemX = [7, 6, 4, 7, 6]
    itemY = [8, 1, 7, 10, 3]
    result = [17, 11, 9, 15, 10]

    for t in range(5):
        main(t, rectangle[t], characterX[t], characterY[t], itemX[t], itemY[t], result[t])
