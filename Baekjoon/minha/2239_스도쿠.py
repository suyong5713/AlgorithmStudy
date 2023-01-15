def rowColCheck(ty, tx, tn):
    for i in range(9):
        if board[ty][i] == tn:
            return False
        if board[i][tx] == tn:
            return False
    return True

def squareCheck(ty, tx, tn):
    ty = ty // 3 * 3
    tx = tx // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[ty + i][tx + j] == tn:
                return False
    return True

def backtracking(num):
    if num == len(zero):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        exit()

    ty, tx = zero[num]
    for tn in range(1, 10):
        if rowColCheck(ty, tx, tn) and squareCheck(ty, tx, tn):
            board[ty][tx] = tn
            backtracking(num + 1)
            board[ty][tx] = 0


board = [list(map(int, input().strip())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]

backtracking(0)