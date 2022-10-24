def divide(x, y, d1, d2):
    edge = [[False] * (N + 1) for _ in range(N + 1)]

    # 1번과 4번 경계선
    for i in range(0, d1 + 1):
        edge[x + i][y - i] = True
        edge[x + d2 + i][y + d2 - i] = True

    # 2번과 3번 경계선
    for i in range(0, d2 + 1):
        edge[x + i][y + i] = True
        edge[x + d1 + i][y - d1 + i] = True

    # 1번 선거구: 1 ≤ r < x + d1, 1 ≤ c ≤ y
    city_1 = 0
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if edge[r][c]:
                break
            city_1 += A[r][c]

    # 2번 선거구: 1 ≤ r ≤ x + d2, y < c ≤ N
    city_2 = 0
    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if edge[r][c]:
                break
            city_2 += A[r][c]

    # 3번 선거구: x + d1 ≤ r ≤ N, 1 ≤ c < y - d1 + d2
    city_3 = 0
    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            if edge[r][c]:
                break
            city_3 += A[r][c]

    # 4번 선거구: x + d2 < r ≤ N, y - d1 + d2 ≤ c ≤ N
    city_4 = 0
    for r in range(x + d2 + 1, N + 1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if edge[r][c]:
                break
            city_4 += A[r][c]

    # 5번 선거구
    city_5 = sum(sum(A, [])) - (city_1 + city_2 + city_3 + city_4)

    cities = [city_1, city_2, city_3, city_4, city_5]
    return max(cities) - min(cities)


N = int(input())
A = [[0] * N]

for _ in range(N):
    A.append([0] + list(map(int, input().split())))

answer = 1e9

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if not (1 <= x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N):
                    continue
                answer = min(answer, divide(x, y, d1, d2))

print(answer)