from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    sum_list = []

    for i in combinations(num, 3):
        sum_list.append(sum(i))

    sum_sort = sorted(list(set(sum_list)), reverse=True)

    print("#{} {}".format(test_case, sum_sort[4]))