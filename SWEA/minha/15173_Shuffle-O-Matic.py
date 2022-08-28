# dial 번호의 다이얼로 카드 섞기
def shuffle(dial, card):
    half_idx = N//2
    l_cnt, r_cnt = 0, 0
    n_card = []

    # 절반씩 로직이 비슷해서 dial 번호에 따라 왼쪽, 오른쪽 덱을 반대로 두고, 횟수 카운트를 위한 n_dial을 따로 둠
    if dial < half_idx:
        l = card[:half_idx]
        r = card[half_idx:]
        n_dial = half_idx - dial - 1
    else:
        l = card[half_idx:]
        r = card[:half_idx]
        n_dial = dial - half_idx

    while l_cnt < half_idx:
        n_card.append(l[l_cnt])
        if l_cnt >= n_dial:
            n_card.append(r[r_cnt])
            r_cnt += 1
        l_cnt += 1

    while r_cnt < half_idx:
        n_card.append(r[r_cnt])
        r_cnt += 1

    return n_card

def dfs(cards, cnt):
    global res

    # 섞는 횟수가 5번 초과이거나, 현재 최솟값보다 크다면 리턴
    if cnt > 5 or cnt >= res:
        return

    # 카드가 정렬됐다면 현재 최솟값과 비교 후 리턴
    if cards == csa or cards == csd:
        res = min(res, cnt)
        return

    # 0~N-1 dial 확인
    for i in range(N):
        dfs(shuffle(i, cards), cnt + 1)

T = int(input())

for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    csa = sorted(cards)
    csd = sorted(cards, reverse=True)
    res = 1e9

    dfs(cards, 0)

    if res > 5:
        print("#{} {}".format(tc + 1, -1))
    else:
        print("#{} {}".format(tc + 1, res))