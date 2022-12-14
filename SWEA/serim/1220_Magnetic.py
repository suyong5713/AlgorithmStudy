for test_case in range(1, 11):
    result = 0
    n = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n - 1):
        for j in range(n):
            if magnetic[i][j] == 1:
                if magnetic[i + 1][j] == 2:
                    result += 1
                elif magnetic[i + 1][j] == 0:
                    magnetic[i + 1][j] = magnetic[i][j]

    print("#{} {}".format(test_case, result))