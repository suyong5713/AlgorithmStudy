from itertools import permutations
from collections import deque

N = int(input())
A = deque(map(int, input().split()))
inpOp = list(map(int, input().split()))

# 입력받은 연산자 갯수에 따라 ops 리스트에 연산자 넣기
ops = []
for _ in range(inpOp[0]):
    ops.append('+')
for _ in range(inpOp[1]):
    ops.append('-')
for _ in range(inpOp[2]):
    ops.append('*')
for _ in range(inpOp[3]):
    ops.append('/')

# ops 리스트 순열 구하기
ops = list(permutations(ops, N - 1))

res = []
# 연산자 순열에서 하나씩 계산 실행
for op in ops:
    nums = A.copy() # 숫자 pop할거라 원본 보존을 위해 nums에 복사
    calcRes = nums.popleft()
    op = deque(op)

    # 연산자와 숫자가 사라질 때까지
    while op and nums:
        # 연산자와 숫자를 하나씩 뽑아서 계산 실행
        o = op.popleft()
        n = nums.popleft()
        if o == '+':
            calcRes += n
        elif o == '-':
            calcRes -= n
        elif o == '*':
            calcRes *= n
        elif o == '/':
            # 문제에서 제시한 음수 나누기, C++14 기준
            if calcRes < 0:
                calcRes = -((-calcRes) // n)
            else:
                calcRes //= n
    res.append(calcRes)

print(max(res))
print(min(res))