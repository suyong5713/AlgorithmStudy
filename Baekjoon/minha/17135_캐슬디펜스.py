from itertools import combinations
import copy

def attack(archer):
    attackL = []
    cnt = 0

    for a in archer:
        target = []
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 1:
                    dis = abs(i - N) + abs(j - a)
                    if dis <= D:
                        target.append([i, j, dis])

        target.sort(key=lambda x: (x[2], x[1]))
        if target:
            attackL.append(target[0])

    for i, j, dis in attackL:
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1

    return cnt

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
pos = [i for i in range(M)]
res = -1

for archer in combinations(pos, 3):
    temp = copy.deepcopy(graph)
    cnt = 0

    while sum(temp, []).count(1) != 0:
        cnt += attack(archer)

        for i in range(N - 1, 0, -1):
            temp[i] = temp[i - 1]
        temp[0] = [0 for _ in range(M)]

    res = max(res, cnt)

print(res)