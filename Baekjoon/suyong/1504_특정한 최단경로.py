import heapq

N, E = map(int,input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    start, end, dist = map(int,input().split())
    graph[start].append([end, dist])
    graph[end].append([start, dist])
v1, v2 = map(int,input().split())

def dijkstra(start_node):
    dp = [float('inf')] * (N + 1)
    dp[start_node] = 0
    queue = []
    heapq.heappush(queue, [0, start_node])
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > dp[node]:
            continue
        for i in graph[node]:
            next_node = i[0]
            next_cost = i[1] + cost
            if next_cost < dp[next_node]:
                dp[next_node] = next_cost
                heapq.heappush(queue, [next_cost, next_node])
    return dp

one_to_all = dijkstra(1)
v1_to_all = dijkstra(v1)
v2_to_all = dijkstra(v2)
answer = min(one_to_all[v1] + v1_to_all[v2] + v2_to_all[N], one_to_all[v2] + v2_to_all[v1] + v1_to_all[N])
print(answer if answer < float("inf") else -1)
