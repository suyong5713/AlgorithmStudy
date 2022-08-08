for tc in range(10):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for j in range(100):
        status = False

        for i in range(100):
            if data[i][j] == 1 and status == False:
                status = True
            elif data[i][j] == 2 and status == True:
                status = False
                result += 1

    print('#{} {}'.format(tc + 1, result))
