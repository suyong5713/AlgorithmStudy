from collections import deque

MAX = 100001

def solution():
    while queue:
        x = queue.popleft()
        if x == k:
            return check[x] - 1
        if x * 2 <= MAX and not check[x * 2]:
            queue.appendleft(x * 2)
            check[x * 2] = check[x]
        if x + 1 <= MAX and not check[x + 1]:
            queue.append(x + 1)
            check[x + 1] = check[x] + 1
        if 0 <= x - 1 and not check[x - 1]:
            queue.append(x - 1)
            check[x - 1] = check[x] + 1


n, k = map(int, input().split())
check = [0] * MAX
queue = deque()
queue.append(n)
check[n] = 1
print(solution())