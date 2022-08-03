maxScore = 0
maxKcal = 0

def search_data(index, score, kcal, data, n):
    global maxScore
    global maxKcal

    if kcal > maxKcal:
        return

    if maxScore < score:
        maxScore = score

    if index == n: # 모두 탐색한 경우
        return

    search_data(index + 1, score + data[index][0], kcal + data[index][1], data, n)
    search_data(index + 1, score, kcal, data, n)

def main():
    global maxScore
    global maxKcal

    test_case = int(input())

    for tc in range(test_case):
        # N: 재료 개수, L: 최대 칼로리
        n, l = map(int, input().split())
        maxKcal = l

        data = []
        for d in range(n):
            # T: 재료 점수, K: 칼로리
            t, k = map(int, input().split())
            data.append([t, k])

        search_data(0, 0, 0, data, n)
        print('#{} {}'.format(tc + 1, maxScore))

        maxScore = 0    # 테스트케이스마다 초기화시켜야함!!

if __name__ == '__main__':
    main()
