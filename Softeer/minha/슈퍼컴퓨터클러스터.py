import math

# min값이 정답일 때 cost를 계산해서 B보다 크면 최솟값을 만들 수 없으므로 false, 아니면 true 반환
def is_possible(min):
    cost = 0
    for ai in A:
        if ai < min:
            cost += (min - ai) ** 2
            if cost > B:
                return False

    return True

N, B = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

left = A[0]
right = A[-1] + int(math.sqrt(B))
answer = 0

while left <= right:
    tmp_min = (left + right) // 2

    if is_possible(tmp_min):
        left = tmp_min + 1
        answer = tmp_min
    else:
        right = tmp_min - 1

print(answer)