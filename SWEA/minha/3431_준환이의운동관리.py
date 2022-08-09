T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())

    if X < L:
        res = L - X
    else:
        if X > U:
            res = -1
        else:
            res = 0

    print("#{} {}".format(test_case, res))
