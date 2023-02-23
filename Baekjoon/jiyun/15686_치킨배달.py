from itertools import combinations
HOUSE, CHICKEN = 1, 2
MAX = 1e9

def solution(_num) -> int:
    result = MAX
    for comb in combinations(chicken, m):
        city_dist = 0
        for h in house:
            house_dist = MAX
            for x in comb:
                house_dist = min(house_dist, abs(h[0] - x[0]) + abs(h[1] - x[1]))
            city_dist += house_dist
        result = min(result, city_dist)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(n)]
    house, chicken = [], []
    for r in range(n):
        for c in range(n):
            if city[r][c] == HOUSE:
                house.append([r, c])
            elif city[r][c] == CHICKEN:
                chicken.append([r, c])
    print(solution(m))