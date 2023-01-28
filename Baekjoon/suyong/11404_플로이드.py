n = int(input())
m = int(input())
cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    # 같은 버스노선 중 저렴한것 저장
    cost[a][b] = min(cost[a][b], c)
# k => 중간에 거쳐갈 지역. 1 ~ n까지 바꿔가며 i ~ j까지 가는 최소 비용을 구함.
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            # i -> j or i -> k -> j 중 가장 저렴한 경우를 저장
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()