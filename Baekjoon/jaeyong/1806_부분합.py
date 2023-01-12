# https://www.acmicpc.net/problem/1806
# 부분합, 투 포인터

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
result = 1e9

sums = nums[0]

while True:
    if sums >= s:
        result = min(result, end - start)
        sums -= nums[start]
        start += 1
    else:
        end += 1
        if end == n:
            break

        sums += nums[end]

print(0 if result == 1e9 else result + 1)
