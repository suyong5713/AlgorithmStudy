from collections import Counter
import itertools
def solution(orders, course):
    answer = []
    for course_length in course:
        course_menu = []
        for order in orders:
            #하나의 주문에서 코스요리 길이만큼 선택해서 조합 생성
            course_menu.extend(map(list,itertools.combinations(order, course_length)))
        for i in range(len(course_menu)):
            #AB와 BA는 같은 코스이기 때문에 코스메뉴를 정렬
            course_menu[i] = ''.join(sorted(course_menu[i]))
        #가장 많이 주문된 코스 조합 추출
        counter = Counter(course_menu).most_common()
        if counter == []: continue
        max_count = counter[0][1]
        #코스 최소길이 2
        if max_count < 2:
          continue
        #row -> (코스, 주문 수)
        #가장 많이 주문된 코스가 다수이면 모두 저장
        for row in counter:
          if row[1] == max_count:
            answer.append(row[0])
    answer.sort()
    return answer