def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

graph = []
for i in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

graph.sort(key=lambda x: x[2])

parent = [0]
for i in range(1, N + 1):
    parent.append(i)

mst_cost = 0
mst_max = -1
last_cost = 0

for idx, edge in enumerate(graph):
    u, v, wt = edge
    if find(u) != find(v):
        union(u, v)
        mst_cost += wt
        last_cost = wt

print(mst_cost - last_cost)