# https://www.acmicpc.net/problem/14501
# 퇴사

import sys

max_sum = -sys.maxsize
n = int(input())
data = [[0, 0]]

def dfs(day, _sum):
    global max_sum
    
    t = data[day][0]
    p = data[day][1]
    
    if day + t > n + 1:
        max_sum = max(max_sum, _sum)
        return
    elif day + t == n + 1:
        max_sum = max(max_sum, _sum + p)
        return
    
    for i in range(day + t, n + 1):
        dfs(i, _sum + p)

for i in range(1, n + 1):
    data.append(list(map(int, input().split())))

for i in range(1, n + 1):
    dfs(i, 0)
    
print(max_sum)
