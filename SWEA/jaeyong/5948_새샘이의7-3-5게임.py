FIND_NUM = 5

def comb_result(num_list):
    result = []

    for i in range(0, len(num_list)):
        for j in range(i + 1, len(num_list)):
            for k in range(j + 1, len(num_list)):
                if i == j or j == k or k == i:
                    continue

                sum = num_list[i] + num_list[j] + num_list[k]

                if sum in result:
                    continue

                result.append(sum)

    result.sort(reverse=True)
    return result

def main():
    test_case = int(input())

    for tc in range(test_case):
        num_list = list(map(int, input().split()))
        result = comb_result(num_list)

        print('#{} {}'.format(tc + 1, result[FIND_NUM - 1]))

if __name__ == '__main__':
    main()
