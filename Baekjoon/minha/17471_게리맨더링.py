from itertools import combinations
from collections import deque

def bfs(g):
    q = deque()
    q.append(g[0])

    visited = [False for _ in range(N)]
    visited[g[0]] = True
    pop = 0
    cnt = 1

    while q:
        node = q.popleft()
        pop += population[node]
        for n in graph[node]:
            if n in g and not visited[n]:
                visited[n] = True
                cnt += 1
                q.append(n)

    return pop, cnt

N = int(input())
city = [i for i in range(N)]
population = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(N):
    con = list(map(int, input().split()))
    for j in con[1:]:
        graph[i].append(j-1)

groupA = []
for cnt in range(1, N//2 + 1):
    for c in combinations(city, cnt):
        groupA.append(list(c))

res = 1e9
for a in groupA:
    b = list(set(city) - set(list(a)))
    pa, na = bfs(a)
    pb, nb = bfs(b)

    if na + nb == N:
        res = min(res, abs(pa - pb))

if res == 1e9:
    print(-1)
else:
    print(res)