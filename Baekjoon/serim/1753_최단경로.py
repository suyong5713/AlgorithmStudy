import heapq


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(queue, [0, start])
    while queue:
        dist, now_node = heapq.heappop(queue)
        if distance[now_node] < dist:
            continue
        for next_node, weight in graph[now_node]:
            next_w = dist + weight
            if next_w < distance[next_node]:
                distance[next_node] = next_w
                heapq.heappush(queue, [next_w, next_node])


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
distance = [1e9] * (V + 1)
queue = []

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(K)

for i in distance[1:]:
    print(i if i != 1e9 else "INF")
