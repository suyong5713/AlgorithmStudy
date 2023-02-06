from itertools import combinations

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
res = 1e9

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, M))

for c in comb_chicken:
    city_chicken = 0
    for x1, y1 in house:
        house_min = 1e9
        for x2, y2 in c:
            house_min = min(house_min, manhattan(x1, y1, x2, y2))
        city_chicken += house_min
    res = min(res, city_chicken)

print(res)