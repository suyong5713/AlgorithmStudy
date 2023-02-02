import heapq

# 정점의 갯수(V), 간선의 갯수(E), 시작점 노드(K)
V, E = map(int, input().split())
K = int(input())

# 경로 입력
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 거리 무한대로 초기화
INF = int(1e9)
distance = [INF] * (V+1)

def dijkstra(start):
    # 시작점 자신인 경우 값은 0
    distance[start] = 0
    # (시작점의 거리, 시작점 노드) heap에 삽입 - 순서 중요
    myHeap = []
    heapq.heappush(myHeap, (0, start))

    while myHeap:
        # 힙에서 현재 거리가 최소인 값을 뽑아 cur_w, cur_n에 해당 노드의 거리, 노드 번호 지정
        cur_w, cur_n = heapq.heappop(myHeap)

        # cur_w가 최솟값이 아니라면(이미 처리된 적 있는 노드라면) continue
        if distance[cur_n] < cur_w:
            continue

        for next_n, weight in graph[cur_n]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            # 다른 노드의 최솟값 갱신하고 힙에 해당 정보 삽입
            if cur_w + weight < distance[next_n]:
                distance[next_n] = cur_w + weight
                heapq.heappush(myHeap, (cur_w + weight, next_n))

dijkstra(K)

for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")