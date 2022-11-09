N, C = map(int, input().split())
M = int(input())

# 보내는 마을, 받는 마을, 박스 개수
village = [list(map(int, input().split())) for _ in range(M)]
village.sort(key=lambda x: (x[1]))

res = 0
capacity = [C for _ in range(N + 1)]

for start, destination, cnt in village:
    cnt = min(cnt, min(capacity[start:destination]))
    if cnt != 0:
        for i in range(start, destination):
            capacity[i] -= cnt
        res += cnt

print(res)