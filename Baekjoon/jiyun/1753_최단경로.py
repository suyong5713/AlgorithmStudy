# 다익스트라 : 특정 한 정점에서 다른 정점으로 가는 각각의 최단 경로를 구해주는 알고리즘
# 버전 2 : 우선 순위 큐(가장 우선 순위가 높은 데이터를 먼저 삭제하는 자료구조) 활용 구현
#         -> 리스트 or PriorityQueue or Heap인데 Heap이 최고임.(삽입/삭제 : O(logN))
#         -> 최소 힙(Min Heap)은 힙에서 원소를 꺼내면 '가장 값이 작은 원소'가 추출됨


from collections import defaultdict
import heapq
INF = int(1e9)


def dijkstra(_start, _vertexN):
    queue = []
    heapq.heappush(queue, (0, _start))                      # 시작 노드 초기화 (거리, 노드 번호)
    distance[_start] = 0
    while queue:
        now_distance, now_vertex = heapq.heappop(queue)     # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (now_vertex == smallest_vertex)
        if distance[now_vertex] < now_distance: continue    # 이미 더 최단 거리가 등록 되어 있는 경우(=이미 처리된 경우), 무시
        for next_vertex, next_weight in graph[now_vertex]:  # 현재 최단 거리인 노드와 연결된 다른 노드 확인
            weight = now_distance + next_weight
            if weight<distance[next_vertex]:                    # 현재 최단 거리 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우 -> 갱신
                distance[next_vertex] = weight
                heapq.heappush(queue, (weight, next_vertex))
    return

def makeGraph(_edges) -> dict:
    temp = defaultdict(list)
    for _ in range(_edges):
        u, v, w = map(int, input().split())
        temp[u].append((v, w))
    return temp

vertex, edge = map(int, input().split())                    # 노드 개수, 간선 개수
start = int(input())                                        # 시작 노드
graph = makeGraph(edge)
distance = [INF] * (vertex+1)                               # 1차원 최단 거리 테이블
dijkstra(start, vertex)
for answer in distance[1:]:
    if answer==INF : print("INF")
    else : print(answer)
