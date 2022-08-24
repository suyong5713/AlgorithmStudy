import copy
def update(dir, cctv):
    global office

    dir = dir % 4
    y = cctv[0]
    x = cctv[1]

    if dir == 0: # 동
        for i in range(x + 1, M):
            if office[y][i] == 6: break
            office[y][i] = '#'
    elif dir == 1:  # 북
        for i in range(y - 1, -1, -1):
            if office[i][x] == 6: break
            office[i][x] = '#'
    elif dir == 2:  # 서
        for i in range(x - 1, -1, -1):
            if office[y][i] == 6: break
            office[y][i] = '#'
    else: # 남
        for i in range(y + 1, N):
            if office[i][x] == 6: break
            office[i][x] = '#'

def dfs(cctv_idx):
    global res
    global office

    # 마지막 cctv까지 확인했다면
    if cctv_idx == len(cctv):
        size = sum(office, []).count(0)
        res = min(res, size)
        return

    type = cctv[cctv_idx][2]
    for d in range(rot[type]):
        temp = copy.deepcopy(office)
        if type == 0:
            update(d, cctv[cctv_idx])
        elif type == 1:
            update(d, cctv[cctv_idx])
            update(d + 2, cctv[cctv_idx])
        elif type == 2:
            update(d, cctv[cctv_idx])
            update(d + 1, cctv[cctv_idx])
        elif type == 3:
            update(d, cctv[cctv_idx])
            update(d + 1, cctv[cctv_idx])
            update(d + 2, cctv[cctv_idx])
        else:
            update(d, cctv[cctv_idx])
            update(d + 1, cctv[cctv_idx])
            update(d + 2, cctv[cctv_idx])
            update(d + 3, cctv[cctv_idx])
        dfs(cctv_idx + 1)
        office = copy.deepcopy(temp)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j] - 1])

rot = [4, 2, 4, 4, 1]
res = 1e9
dfs(0)

print(res)