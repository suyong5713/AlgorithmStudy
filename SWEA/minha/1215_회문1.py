T = 10
for test_case in range(0, T):
    def find_pd(arr):
        pd_cnt = 0
        last_idx = 8 - pd_length
        for start in range(last_idx + 1):
            s = arr[start:start + pd_length]
            if s == s[::-1]:
                pd_cnt += 1
        return pd_cnt

    pd_length = int(input())

    graph = []
    for i in range(8):
        row = input()
        graph.append(list(row))
    col_graph = list(map(list, zip(*graph)))

    total_cnt = 0
    for i in range(8):
        total_cnt += find_pd(graph[i])
        total_cnt += find_pd(col_graph[i])

    print("#{} {}".format(test_case + 1, total_cnt))
