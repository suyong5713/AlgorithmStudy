import math

def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

N = int(input())

if N == 1:
    print(0)
else:
    # N까지의 소수값 primes 리스트에 넣기
    primes = []

    for n in range(N + 1):
        if is_prime_number(n):
            primes.append(n)

    answer = 0
    start = 0
    end = 0
    tot = primes[0]

    while end < len(primes):
        # 합이 같아지면 카운트 후, 왼쪽과 오른쪽 모두 한칸씩 이동
        if tot == N:
            answer += 1
            tot -= primes[start]
            start += 1
            end += 1
            if end == len(primes):
                break
            tot += primes[end]
        # 합이 N보다 크면 현재 시작값을 뺀 후 시작 위치 한 칸 이동
        elif tot > N:
            tot -= primes[start]
            start += 1
        # 합이 N보다 작으면 끝 위치 한 칸 이동 후 이동된 위치의 끝 값 더함
        else:
            end += 1
            if end == len(primes):
                break
            tot += primes[end]

    print(answer)