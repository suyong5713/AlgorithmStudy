import copy


def dfs(row, col, grid, position, n, target):
    res = [position]
    for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        n_row, n_col = row + dir[0], col + dir[1]
        if 0 <= n_row < n and 0 <= n_col < n and grid[n_row][n_col] == target:
            grid[n_row][n_col] = 2
            res += dfs(n_row, n_col, grid, [position[0] + dir[0], position[1] + dir[1]], n, target)
    return res


def rotate(arr):
    # 전치시킨 후 반대로 뒤집으면 90도 반시계 회전
    rotate_arr = list(map(list, zip(*arr)))[::-1]
    return rotate_arr


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    block_list = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                game_board[i][j] = 2
                # 블럭 모양 찾아서 저장
                block = dfs(i, j, game_board, [0, 0], n, 0)
                block_list.append(block)
    # 4회 회전
    for _ in range(4):
        table = rotate(table)
        table_copy = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if table_copy[i][j] == 1:
                    table_copy[i][j] = 2
                    block = dfs(i, j, table_copy, [0, 0], n, 1)
                    # 테이블에서 찾은 블럭이 게임 보드에서 찾은 블럭과 일치하면,
                    if block in block_list:
                        # 게임 보드 블럭에서 제거
                        block_list.pop(block_list.index(block))
                        answer += (len(block))
                        # 현재 테이블 상태를 갱신
                        table = copy.deepcopy(table_copy)
                    else:
                        # 테이블에 2로 표시했던 칸들 롤백
                        table_copy = copy.deepcopy(table)
    return answer
