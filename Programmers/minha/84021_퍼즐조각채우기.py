from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find_block(y, x, table):
    # 리턴할 결과는 블록의 중복되지 않는 y, x 값
    res = [{y}, {x}]
    q = deque()
    q.append((y, x))

    # bfs 돌면서
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 블록이 존재하는 칸이면
            if 0 <= ny < len(table) and 0 <= nx < len(table) and table[ny][nx] == 1:
                # 리턴 결과값에 y, x값 각각 더하기
                res[0].add(ny)
                res[1].add(nx)
                # table 바꿔주고
                table[ny][nx] = 0
                # 큐에 값 넣기
                q.append((ny, nx))

    return res

def change_coord_to_shape(puzzle, table):
    res = []

    for ys, xs in puzzle:
        # 블록 좌표의 y, x 각각 최소, 최대값 구하기
        min_y = min(ys)
        min_x = min(xs)
        max_y = max(ys)
        max_x = max(xs)

        # table의 형태 그대로 가져와서 res에 저장
        row = []
        for y in range(min_y, max_y + 1):
            row.append(table[y][min_x:max_x + 1])
        res.append(row)

    return res

# 90도씩 회전시키는 함수
def rotate(block):
    res = []
    # 열이 같은 것들을 뒤집어서 res에 한줄씩 저장
    for item in zip(*block):
        res.append(list(reversed(item)))

    return res

def solution(game_board, table):
    # 블럭 찾아서 블럭의 y, x 좌표 집합 p_loc에 담아주기
    # 문제에서 2번 블록의 경우 [{0, 1, 2}, {3, 4, 5}]로 담아줌
    p_loc = []
    c_table = [t[:] for t in table]
    for ty in range(len(c_table)):
        for tx in range(len(c_table)):
            if c_table[ty][tx] == 1:
                c_table[ty][tx] = 0
                p_loc.append(find_block(ty, tx, c_table))

    # 블럭 좌표가 아닌 모양으로 바꾸기
    # 문제에서 2번 블록의 경우 [[1, 1, 0], [0, 1, 0], [0, 1, 1]]가 됨
    blocks = change_coord_to_shape(p_loc, table)

    # 블럭 각각 회전한 것들을 딕셔너리로 저장, 키는 blocks 리스트에서 인덱스 번호로 설정
    rot_blocks = dict()
    for idx, block in enumerate(blocks):
        rot_blocks[idx] = [block]
        for _ in range(3):
            block = rotate(block)
            rot_blocks[idx].append(block)

    # 블럭과 빈공간 찾을 때 같은 함수 사용하기 위해 game_board에서 빈 공간을 1로, 블럭 공간을 0으로 바꿔줌
    for by in range(len(game_board)):
        for bx in range(len(game_board)):
            if game_board[by][bx] == 1:
                game_board[by][bx] = 0
            else:
                game_board[by][bx] = 1

    # 빈공간 찾아서 빈공간의 y, x 좌표 집합 e_loc에 담아주기
    e_loc = []
    c_game_board = [g[:] for g in game_board]
    for ty in range(len(c_game_board)):
        for tx in range(len(c_game_board)):
            if c_game_board[ty][tx] == 1:
                c_game_board[ty][tx] = 0
                e_loc.append(find_block(ty, tx, c_game_board))

    # 빈공간 좌표가 아닌 모양으로 바꾸기
    empties = change_coord_to_shape(e_loc, game_board)

    # 빈공간 하나씩 블럭이랑 맞춰보면서 맞는 블럭 인덱스 번호 target_block_idx에 저장
    # 반복문에서 삭제하는거 처리하기 번거롭고 1인거 갯수 세야해서 target_block_idx에 저장함
    target_block_idx = []
    for e in empties:
        # 빈칸에 맞는 블럭 찾았는지 플래그
        # 문제에서 4, 5번 블록 회전했을 때 똑같은 모양 -> game_board 우상단에 중복으로 들어가는거 막기 위해
        flag = False
        # 블럭별로 인덱스와 회전 목록
        for idx, r_blocks in rot_blocks.items():
            # 빈공간과 일치하는 블럭이 회전 목록에 존재하고, 사용하지 않은 블럭이라면
            # target_block_idx에 인덱스 넣어주고 플래그 True로 바꿔주기
            if e in r_blocks and idx not in target_block_idx:
                target_block_idx.append(idx)
                flag = True
            # 빈칸에 맞는 블럭 찾았다면 블럭 탐색하는 반복문 탈출
            if flag:
                break

    # target_block_idx의 인덱스 반복문 돌면서 그 블록에 1 몇개인지 세서 answer에 더해줌
    answer = 0
    for idx in target_block_idx:
        answer += sum(blocks[idx], []).count(1)

    return answer

solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0]],
         [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
          [0, 1, 0, 0, 0, 0]])