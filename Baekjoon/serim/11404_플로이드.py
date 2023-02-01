n = int(input())
m = int(input())
cost = [[1e9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a - 1][b - 1] = min(c, cost[a - 1][b - 1])
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for i in cost:
    for j in i:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()