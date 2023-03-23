import sys
sys.setrecursionlimit(10**6)

# V -> L -> R
# L -> R -> V
def dfs(left, right):
    if left > right:
        return
    else:
        mid = right + 1
        for i in range(left + 1, right + 1):
            if num[left] < num[i]:
                mid = i
                break
        dfs(left + 1, mid - 1)
        dfs(mid, right)
        print(num[left])

num = []
while True:
    try:
        num.append(int(input()))
    except:
        break

dfs(0, len(num) - 1)