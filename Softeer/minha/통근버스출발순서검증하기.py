n = int(input())
nums = [0] + list(map(int, input().split()))

arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for x in range(1, n + 1):
    arr[x][n] = 0
    arr[x][n - 1] = 1 if nums[n] < x else 0
    for j in range(n - 2, 0, -1):
        if nums[j + 1] < x:
            arr[x][j] = arr[x][j + 1] + 1
        else:
            arr[x][j] = arr[x][j + 1]

cnt = 0
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if nums[i] < nums[j]:
            cnt += arr[nums[i]][j]

print(cnt)