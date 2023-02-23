import itertools

N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
house, store = [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            store.append([i,j])
answer = float("inf")

for chicken in itertools.combinations(store, M):
    city_chicken_distance = 0
    for h in house:
        home_to_store = float('inf')
        for m in range(M):
            home_to_store = min(home_to_store, abs(h[0] - chicken[m][0]) + abs(h[1] - chicken[m][1]))
        city_chicken_distance += home_to_store
    answer = min(city_chicken_distance, answer)
print(answer)