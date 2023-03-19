N = int(input())
numbers = list(map(int, input().split()))

dp_increase = [1] * N
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

dp_decrease = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if numbers[i] > numbers[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

bitonic = [-1] * N
for i in range(N):
    bitonic[i] = dp_increase[i] + dp_decrease[i]

print(max(bitonic) - 1)