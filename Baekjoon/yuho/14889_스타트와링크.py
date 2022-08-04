from itertools import combinations
import math

def calc_sum(case):
    sum = 0
    l = len(case)
    for i in range(l):
        for j in range(i+1,l):
            sum += (arr[case[i]][case[j]] + arr[case[j]][case[i]])
    # for i,j in list(combinations(case,2)):
    #     sum += (arr[i][j] + arr[j][i])
    return sum

n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]
min_res = math.inf
caseList = list(combinations(range(n),n//2))
for i in range(len(caseList)//2):
    res = abs(calc_sum(caseList[i]) - calc_sum(caseList[(i+1)*(-1)]))
    if min_res > res:
        min_res = res
print(min_res)