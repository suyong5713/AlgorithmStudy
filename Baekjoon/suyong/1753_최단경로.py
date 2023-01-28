import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] * (V + 1) for _ in range(V + 1)]
distance = [float('inf')] * (V + 1)
for _ in range(E):
    start, end, dist = map(int, input().split())
    graph[start].append([end, dist])
queue = []
heapq.heappush(queue, [0, K])
distance[K] = 0
while queue:
    dist, current = heapq.heappop(queue)
    # 현재 노드까지의 거리가 이미 계산되어있고 더 짧다면 continue,
    # 같다면 현재노드를 통해 다른 노드로 이동하는 최단경로가 존재할 수 있기 때문에 continue X
    if distance[current] < dist:
        continue
    # 현재 노드를 통해 갈 수 있는 노드 탐색
    for i in graph[current]:
        # 현재 노드를 통해 다음 노드를 갈 때 총 거리
        total_dist = dist + i[1]
        # 현재노드를 경유해 다음노드로 가는 방법이 최단경로일
        if total_dist < distance[i[0]]:
            distance[i[0]] = total_dist
            heapq.heappush(queue, [total_dist, i[0]])
for i in distance[1:]:
    print("INF") if i == float('inf') else print(i)
