import copy


def left(board):
    result = []
    for row in board:
        stack = []
        for i in row:
            if i == 0:
                continue
            if stack and stack[-1] == i:
                stack[-1] = stack[-1] * 2 + 1
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i] % 2 == 1:
                stack[i] -= 1
        while len(stack) != N:
            stack.append(0)
        result.append(stack)
    return result


def right(board):
    result = []
    for row in board:
        stack = []
        for i in row[::-1]:
            if i == 0:
                continue
            if stack and stack[-1] == i:
                stack[-1] = stack[-1] * 2 + 1
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i] % 2 == 1:
                stack[i] -= 1
        while len(stack) != N:
            stack.append(0)
        result.append(stack[::-1])
    return result


def up(board):
    result = []
    for col in zip(*board):
        stack = []
        for i in col:
            if i == 0:
                continue
            if stack and stack[-1] == i:
                stack[-1] = stack[-1] * 2 + 1
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i] % 2 == 1:
                stack[i] -= 1
        while len(stack) != N:
            stack.append(0)
        result.append(stack)

    return list(zip(*result))


def down(board):
    result = []
    for col in zip(*board):
        stack = []
        for i in col[::-1]:
            if i == 0:
                continue
            if stack and stack[-1] == i:
                stack[-1] = stack[-1] * 2 + 1
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i] % 2 == 1:
                stack[i] -= 1
        while len(stack) != N:
            stack.append(0)
        result.append(stack[::-1])
    return list(zip(*result))

def dfs(depth, board):
    global answer
    if depth == 5:
        for i in range(N):
            for j in range(N):
                if answer < board[i][j]:
                    answer = board[i][j]
        return
    for i in range(4):
        if i == 0:
            dfs(depth + 1, left(copy.deepcopy(board)))
        elif i == 1:
            dfs(depth + 1, right(copy.deepcopy(board)))
        elif i == 2:
            dfs(depth + 1, up(copy.deepcopy(board)))
        else:
            dfs(depth + 1, down(copy.deepcopy(board)))

    return
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0, copy.deepcopy(board))
print(answer)

