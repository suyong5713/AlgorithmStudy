T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    result = 0
    if X > U:
        result = -1
    elif X < L:
        result = L - X
    print("#{} {}".format(test_case, result))