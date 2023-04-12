import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    start, dest, cost = map(int, input().split())
    graph[start].append((dest, cost))

A, B = map(int, input().split())

distance = [1e9] * (N + 1)

def dijkstra(start):
    myHeap = []

    distance[start] = 0
    heapq.heappush(myHeap, (0, start))

    while myHeap:
        cw, cn = heapq.heappop(myHeap)

        if distance[cn] < cw:
            continue

        for nn, nw in graph[cn]:
            if cw + nw < distance[nn]:
                distance[nn] = cw + nw
                heapq.heappush(myHeap, (cw + nw, nn))

dijkstra(A)

print(distance[B])