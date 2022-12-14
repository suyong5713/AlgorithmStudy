from itertools import combinations
from collections import deque

def bfs(area):
    q = deque()
    q.append(area[0])
    visited = [0] * (n + 1)
    visited[area[0]] = 1
    while q:
        now = q.popleft()
        for a in dict.get(now):
            if a in area and visited[a] == 0:
                visited[a] = 1
                q.append(a)
    for i in area:
        if visited[i] == 0:
            return False
    return True

n = int(input())
population = [0] + list(map(int, input().split()))
dict = {}   # 인접한 구역 저장
for i in range(1, n + 1):
    dict[i] = list(map(int, input().split()))[1:]
result = 1e9
diff = 0
for i in range(1, n // 2 + 1):
    for c in combinations([x for x in range(1, n + 1)], i):
        area_one = c
        area_two = [y for y in range(1, n + 1) if y not in area_one]
        if bfs(area_one) and bfs(area_two):
            population_one = sum(population[a] for a in area_one)
            population_two = sum(population[b] for b in area_two)
            diff = abs(population_one - population_two)
            result = min(result, diff)
if result == 1e9:
    result = -1
print(result)