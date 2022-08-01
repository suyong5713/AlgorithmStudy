from collections import deque

def move(x,y,dx,dy):
    distance = 0
    while board[x + dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        distance += 1
    return x,y,distance

def BFS():
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count > 10:
            break
        for i in range(4):
            next_rx, next_ry, r_dist = move(rx,ry,dx[i],dy[i])
            next_bx, next_by, b_dist = move(bx,by,dx[i],dy[i])
            
            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(count) #성공
                return
            if next_rx == next_bx and next_ry == next_by:
                if r_dist > b_dist:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry,next_bx,next_by,count + 1))
    print(-1)

n,m = map(int,input().split())
board = [[] * m for i in range(n)]
dx, dy = [-1,0,1,0],[0,1,0,-1]
q = deque()
visited = [[[[False]*m for _ in range(n)] for i in range(m)] for _ in range(n)]
for i in range(n):
    board[i] = input()
rx,ry,bx,by,count = 0,0,0,0,1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx = i
            ry = j
        elif board[i][j] == 'B':
            bx = i
            by = j
visited[rx][ry][bx][by] = True
q.append((rx,ry,bx,by,count))
BFS()

