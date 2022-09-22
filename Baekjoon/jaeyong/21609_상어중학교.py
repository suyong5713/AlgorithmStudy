# https://www.acmicpc.net/problem/21609
# 상어 중학교

# N x N 격자에서 게임 진행
# 모든 칸에 블록이 하나씩 들어있음

# 검은색 블록 : -1
# 무지개 블록 : 0

# 오토플레이 규칙
# 1. 크기가 가장 큰 블록 그룹을 찾는다
# (우선순위 : 무지개 블록의 수 > 블록의 행 크기 > 블록의 열 크기)
# 2. 1에서 찾은 브록 그룹의 모든 블록 제거 (B ^ 2 점수 획득)
# 3. 격자에 중력이 작용한다
# 4. 격자가 90도 반시계 방향으로 회전한다
# 5. 다시 격자에 중력이 작용한다

from collections import deque
# 게임은 크기가 N×N인 격자에서 진행
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 1. 크기가 가장 큰 블록 그룹을 찾는다.
def find(board):
    # 여러 블록 그룹 중 가장 큰 블록 그룹의 크기
    max_size = 0
    # 가장 큰 블록 그룹의 번호
    max_group = -1
    # 가장 큰 블록 그룹이 가지고 있는 무지개 블록의 수
    max_rainbow = 0
    # 블록 그룹의 번호
    count = 0
    # bfs를 위한 큐
    queue = deque()
    # 각 그룹 블록에 포함되는 좌표 저장
    his = {}
    # 레인보우 블록의 좌표 저장
    rainbow_loc = {}
    # 일반 블록의 좌표 저장
    block_loc = {}
    # 방문 배열 초기화
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 블록 그룹의 크기
            size = 1
            # 블록 그룹에 포함된 레인보우 블록
            rainbow = 0

            # 일반 블록이라면
            if 0 < board[i][j] <= m and visited[i][j] == 0:
                visited[i][j] = 1
                count += 1
                queue.append([i, j])
                color = board[i][j]  # 시작하는 일반 블록의 색상 저장
                his[count] = [[i, j]]
                block_loc[count] = [[i, j]]
                rainbow_loc[count] = []

                while queue:
                    r, c = queue.popleft()

                    for k in range(4):
                        ny = r + dy[k]
                        nx = c + dx[k]

                        if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == color or board[ny][nx] == 0) and visited[ny][nx] == 0:
                            if board[nx][ny] == 0:
                                rainbow += 1
                                rainbow_loc[count].append([ny, nx])
                            else:
                                block_loc[count].append([ny, nx])
                            his[count].append([ny, nx])
                            queue.append([ny, nx])
                            visited[ny][nx] = 1
                            size += 1

                for x, y in rainbow_loc[count]:
                    visited[y][x] = 0

                block_loc[count].sort()

                if max_size < size:
                    max_size = size
                    max_group = count
                    max_rainbow = rainbow
                # 1.1. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
                elif max_size == size:
                    if max_rainbow < rainbow:
                        max_size = size
                        max_group = count
                        max_rainbow = rainbow
                    # 1.2. 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
                    elif max_rainbow == rainbow:
                        if block_loc[max_group][0][0] < block_loc[count][0][0]:
                            max_size = size
                            max_group = count
                            max_rainbow = rainbow
                        # 1.3. 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
                        elif block_loc[max_group][0][0] == block_loc[count][0][0]:
                            if block_loc[max_group][0][1] < block_loc[count][0][1]:
                                max_size = size
                                max_group = count
                                max_rainbow = rainbow

    # max_group이 -1이라면 블록 그룹이 없으므로 게임을 종료한다
    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B**2점을 획득한다.
    if max_group < 1 or max_size < 2:
        return -1, board

    for i in range(n):
        for j in range(n):
            if [i, j] in his[max_group]:
                board[i][j] = 6  # 사라진 곳은 6으로 표시
    return max_size ** 2, board

# 3. 격자에 중력이 작용한다.
# 중력 작용 함수 6 - 빈칸


def move(board):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if board[j][i] != 6 and board[j][i] != -1:
                start = j
                while 0 <= start + 1 < n and board[start + 1][i] == 6:
                    board[start + 1][i] = board[start][i]
                    board[start][i] = 6
                    start += 1

    return board

# 4. 격자가 90도 반시계 방향으로 회전한다.


def rotate(board):
    result = []
    for i in range(n - 1, -1, -1):
        temp = []
        for j in range(0, n):
            temp.append(board[j][i])
        result.append(temp)
    return result

# 5. 다시 격자에 중력이 작용한다.

# 격자에 중력이 작용하면 "검은색 블록을 제외한 모든 블록"이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.


ans = 0
while True:
    s, b = find(board)

    if s == -1:
        break

    ans += s

    m_b = move(b)
    r_b = rotate(m_b)
    m_b = move(r_b)
    board = m_b

print(ans)
