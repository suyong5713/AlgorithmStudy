n = int(input())

for i in range(1, n + 1):
    min, max, now = map(int, input().split())

    if now < min: print('#{} {}'.format(i, min - now))
    elif now > max: print('#{} {}'.format(i, -1))
    else: print('#{} {}'.format(i, 0))
