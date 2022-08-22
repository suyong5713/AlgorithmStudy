# 3줄 코딩 버전
'''
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(''.join(['#{} OFF\n'.format(d+1) if len(str(bin(data[d][1])[2:])) < data[d][0] else ('#{} OFF\n'.format(d+1)
      if '0' in str(bin(data[d][1])[2:])[-data[d][0]:] else '#{} ON\n'.format(d+1)) for d in range(len(data))]))
'''

# 가독성이 좋은 버전의 코드
tc = int(input())                                            # 테스트케이스 수
data = [list(map(int, input().split())) for _ in range(tc)]  # 데이터 입력

tc_num = 1              # 몇 번째 테스트케이스인가?
for d in data:
    n = d[0]            # 마지막 N개의 비트 수
    m = bin(d[1])[2:]   # 이진수로 변환된 십진수

    if len(str(m)) < n:
        print('#{} OFF'.format(tc_num))     # 이진수의 자리수가 N개보다 적을 때 항상 0이 있음
    else:
        if '0' in str(m)[-n:]:
            print('#{} OFF'.format(tc_num)) # 0이 하나라도 있는 경우
        else:
            print('#{} ON'.format(tc_num))  # 모두 1일때만 ON

    tc_num += 1
