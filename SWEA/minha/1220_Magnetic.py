T = 10

for test_case in range(1, T + 1):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(size)]
    col_graph = list(map(list, zip(*graph)))
    res = 0

    for i in range(len(col_graph)):
        check_list = []
        for j in col_graph[i]:
            if j == 1:
                check_list.append(j)
            elif j == 2:
                if len(check_list) != 0:
                    if check_list[-1] == 1:
                        check_list.clear()
                        res += 1
                else:
                    continue
            else:
                continue

    print("#{} {}".format(test_case, res))
