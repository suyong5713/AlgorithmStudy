tc = int(input())
for i in range(1, tc + 1):
    n, m = map(int, input().split())
    # bin을 통해 이진수 변환을 하면 앞에 0b가 붙음
    # 이를 지우기 위해 슬라이싱함
    m = list(map(int, bin(m)[2:]))
    m.reverse()
    if m[:n].count(1) == n:
        print("#{} {}".format(i, 'ON'))
    else:
        print("#{} {}".format(i, 'OFF'))