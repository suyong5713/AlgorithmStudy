from itertools import combinations

T = int(input())

# 방법 1 : 포함 유무를 파악하며 리스트 삽입
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    # 조합을 사용하여 3가지의 숫자를 리스트로 만듬
    num_combi = list(combinations(nums, 3))
    sum_list = list()
    # 각 조합에 대한 합을 구하여 sum_list에 append
    for i in range(len(num_combi)):
        sum = num_combi[i][0] + num_combi[i][1] + num_combi[i][2]
        if sum not in sum_list:
            sum_list.append(sum)
    # 조합에 대한 합을 내림차순으로 정렬
    sum_list.sort(reverse=True)
    # 다섯번째로 큰 수 출력
    print('#{} {}'.format(test_case, sum_list[4]))

# 방법 2 : set 이용
# for test_case in range(1, T + 1):
#     nums = list(map(int, input().split()))
#     num_combi = list(combinations(nums, 3))
#     sum = list()
#
#     for i in range(len(num_combi)):
#         sum.append(num_combi[i][0] + num_combi[i][1] + num_combi[i][2])
#
#     sum = list(set(sum))
#
#     sum = sorted(sum, reverse = True)
#
#     print('#{} {}'.format(test_case, sum[4]))
