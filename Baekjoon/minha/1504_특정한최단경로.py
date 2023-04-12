import heapq

def dijkstra(start):
    distance = [1e9] * (N + 1)

    distance[start] = 0
    my_heap = []
    heapq.heappush(my_heap, (0, start))

    while my_heap:
        cur_w, cur_n = heapq.heappop(my_heap)

        if distance[cur_n] < cur_w:
            continue

        for next_n, weight in graph[cur_n]:
            if cur_w + weight < distance[next_n]:
                distance[next_n] = cur_w + weight
                heapq.heappush(my_heap, (cur_w + weight, next_n))

    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

result = min(start_1[v1] + start_v1[v2] + start_v2[N], start_1[v2] + start_v2[v1] + start_v1[N])
if result < 1e9:
    print(result)
else:
    print(-1)