# 방법 1
def dfs(depth, index):
    global n, result
    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += s[i][j]
                elif not visited[i] and not visited[j]:
                    link += s[i][j]
        result = min(result, abs(start - link))
        return

    for i in range(index, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
result = 1e9
dfs(0, 0)
print(result)


# 방법 2
# from itertools import combinations
# n = int(input())
# nums = [i for i in range(n)]
# result = 1e9
# s = []
# for _ in range(n):
#     s.append(list(map(int, input().split())))
#
# for start in combinations(nums, n//2):
#     link = list(set(nums) - set(start))
#     startSum, linkSum = 0, 0
#     for numStart in combinations(start, 2):
#         startSum += s[numStart[0]][numStart[1]]
#         startSum += s[numStart[1]][numStart[0]]
#     for numLink in combinations(link, 2):
#         linkSum += s[numLink[0]][numLink[1]]
#         linkSum += s[numLink[1]][numLink[0]]
#     result = min(result, abs(startSum - linkSum))
#
# print(result)