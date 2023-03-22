n = int(input())
a = list(map(int, input().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and increase[i] < increase[j] + 1:
            increase[i] = increase[j] + 1

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] > a[j] and decrease[i] < decrease[j] + 1:
            decrease[i] = decrease[j] + 1
    result[i] = decrease[i] + increase[i] - 1

print(max(result))