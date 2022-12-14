from collections import Counter
def rcOperation():
    max_len = 0
    len_numbers = len(numbers)
    for j in range(len_numbers):
        #0이 아닌 값 필터링
        a = [i for i in numbers[j] if i != 0]
        #a배열의 요소개수 카운팅하여 튜플 형태로 반환
        a = Counter(a).most_common()
        #요소 개수로 정렬
        a.sort(key = lambda x : (x[1], x[0]))
        numbers[j] = []
        #정렬된 수를 배열에 다시 저장
        for num, num_count in a:
            numbers[j].append(num)
            numbers[j].append(num_count)
        if max_len < len(numbers[j]):
          max_len = len(numbers[j])
    for j in range(len_numbers):
        for k in range(max_len - len(numbers[j])):
            numbers[j].append(0)
        #열 크기가 100 넘어가면 배열 자르기
        numbers[j] = numbers[j][:100]

R, C, K = map(int, input().split())
numbers = [list(map(int, input().split())) for i in range(3)]
#100초 진행.
for i in range(101):
    try:
      #A[R][C]값이 k가 되면
        if numbers[R - 1][C - 1] == K:
          #시간 출력
            print(i)
            break
      #numbers 배열 크기가 동적으로 바뀌기 때문에 indexOutOfRange처리
    except: pass
    #행보다 열이 크면 C연산
    if len(numbers) < len(numbers[0]):
      #C연산을 열과 행을 반전하여 R연산과 동일하게 처리
        numbers = list(zip(*numbers))
        rcOperation()
      #배열을 원래 형태로 돌림
        numbers = list(zip(*numbers))
    else:
        rcOperation()
else:
    print(-1)