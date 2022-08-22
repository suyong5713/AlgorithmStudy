from itertools import combinations
import copy
import sys
sys.stdin = open("input.txt", "r")

# 두 위치 거리 계산
def cal(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def find(graph, r, c, d):
    enemies = []
    global target
    for i in range(r - 1, 0, -1):
        for j in range(m):
            if graph[i][j] == 1:
                length = cal(r, i, c, j)
                if length <= d:
                    enemies.append((length, j, i))
    if enemies:
        enemies.sort()
        target.append((enemies[0][2], enemies[0][1]))
        return True
    return False


n, m, d = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] = list(map(int, input().split()))
result = 0
temp = 0
shoot = 0
target = []
# 궁수 위치 조합
combi = list(combinations([i for i in range(m)], 3))

for archer in combi:
    graph_copy = copy.deepcopy(graph)
    for r in range(n + 1, 1, -1):
        for c in archer:
            find(graph_copy, r, c, d)
        for enemy in target:
            if graph_copy[enemy[0]][enemy[1]] == 1:
                temp += 1
                graph_copy[enemy[0]][enemy[1]] = 0
        target.clear()
    result = max(result, temp)
    temp = 0

print(result)