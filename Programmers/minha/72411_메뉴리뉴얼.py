from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 단품 메뉴의 갯수 반복문 돌면서
    for cnt in course:
        arr = []
        # 주문 리스트의 한가지씩을 단품 메뉴 갯수만큼 조합으로 구해서 문자열 형태로 arr에 담는다
        for o in orders:
            comb = list(combinations(sorted(o), cnt))
            for c in comb:
                arr.append(''.join(c))

        # cnt개의 조합으로 만들어진 리스트를 카운터로
        counter = Counter(arr)

        # 카운터에 원소가 1개라도 존재하면
        if counter:
            # cnt개의 조합 중 가장 많이 주문된 조합의 갯수가 c_max
            c_max = max(counter.values())

            # 가장 많이 주문된 조합의 갯수가 최소 2명 이상으로부터 주문되었다면
            if c_max > 1:
                # 카운터에서 c_max번 주문된 조합들을 answer에 담기
                for c in counter:
                    if counter[c] == c_max:
                        answer.append(c)

    answer.sort()
    return answer

# tc1 -> result = ["AC", "ACDE", "BCFG", "CDE"]
# ord = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# cou = [2,3,4]
# print(solution(ord, cou))

# tc2 -> result = ["ACD", "AD", "ADE", "CD", "XYZ"]
# ord = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# cou = [2,3,5]
# print(solution(ord, cou))

# tc3 -> result = ["WX", "XY"]
# ord = ["XYZ", "XWY", "WXA"]
# cou = [2,3,4]
# print(solution(ord, cou))