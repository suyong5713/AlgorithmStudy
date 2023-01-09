N = int(input())
prime_flag = [True for _ in range(N + 1)]
prime = []
answer = 0

# 에라토스테네스의 체 (https://loosie.tistory.com/267)
for i in range(2, N//2 + 1):
    if prime_flag[i]:
        j = 2
        while i * j <= N:
            prime_flag[i * j] = False
            j += 1
for num in range(2, N + 1):
    if prime_flag[num]:
        prime.append(num)

end, sub_sum = 0, 0
for start in range(len(prime)):
    while sub_sum < N and end < len(prime):
        sub_sum += prime[end]
        end += 1
    if sub_sum == N:
        answer += 1
    sub_sum -= prime[start]
print(answer)
