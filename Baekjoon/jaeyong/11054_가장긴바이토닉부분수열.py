# https://www.acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열, DP

n = int(input())

case = list(map(int, input().split()))
reverse = case[::-1]

inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if case[i] > case[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if reverse[i] > reverse[j]:
            dec[i] = max(dec[i], dec[j] + 1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = inc[i] + dec[n - i - 1] - 1

print(max(result))
