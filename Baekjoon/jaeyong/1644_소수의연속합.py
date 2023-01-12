# https://www.acmicpc.net/problem/1644
# 소수의 연속합, 투 포인터

def get_primes(n):
    # 처음에는 True로 초기화
    nums = [True] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if nums[i] == True:

            # i의 배수에 대한 수를 전부 False 처리 (에라토스테네스의 채)
            j = 2
            while i * j <= n:
                nums[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if nums[i] == True:
            primes.append(i)
    
    return primes

n = int(input())
primes = get_primes(n)

# 투포인터 로직 시작
result = 0
start, end = 0, 0

size = len(primes)
while end <= size:
    temp = sum(primes[start:end])

    if temp <= n:
        end += 1

        if temp == n:
            result += 1
    
    elif temp > n:
        start += 1

print(result)
