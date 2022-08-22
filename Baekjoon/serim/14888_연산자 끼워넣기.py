def dfs(cnt, result):
    global min_val, max_val
    if cnt == n - 1:
        min_val = min(min_val, result)
        max_val = max(max_val, result)
        return
    for i in range(4):
        if opers[i] >= 1:
            opers[i] -= 1
            if i == 0:
                cur = result + nums[cnt + 1]
            elif i == 1:
                cur = result - nums[cnt + 1]
            elif i == 2:
                cur = result * nums[cnt + 1]
            elif i == 3:
                cur = int(result / nums[cnt + 1])
            dfs(cnt + 1, cur)
            opers[i] += 1


n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
min_val, max_val = 1e9, -1e9
dfs(0, nums[0])
print(max_val)
print(min_val)