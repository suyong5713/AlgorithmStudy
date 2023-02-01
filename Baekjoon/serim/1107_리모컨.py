n = int(input())
m = int(input())
broken = list(input().split())
result = abs(n - 100)
for num in range(1000000):
    num = str(num)
    for i in num:
        if i in broken:
            break
    else:
        result = min(result, abs(n - int(num)) + len(num))
print(result)