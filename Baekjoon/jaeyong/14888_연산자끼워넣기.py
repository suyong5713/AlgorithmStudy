# https://www.acmicpc.net/problem/14888
# DFS / 백트래킹 활용

import sys
from collections import deque

sum_min = sys.maxsize
sum_max = -sys.maxsize

n = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))    # 연산자 (+, -, *, /)


def dfs(num, idx):
    global sum_max, sum_min

    if (idx == n):
        sum_max = max(sum_max, num)
        sum_min = min(sum_min, num)

        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1

            if i == 0:
                dfs(num + data[idx], idx + 1)    # +
            elif i == 1:
                dfs(num - data[idx], idx + 1)  # -
            elif i == 2:
                dfs(num * data[idx], idx + 1)  # *
            elif i == 3:
                if num < 0:
                    dfs(-(-num // data[idx]), idx + 1)  # / (음수)
                else:
                    dfs(num // data[idx], idx + 1)  # / (양수)

            op[i] += 1


dfs(data[0], 1)
print(sum_max)
print(sum_min)
