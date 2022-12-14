def subset_sum(idx, sub_sum_score, sub_sum_calorie):
    global result
    if sub_sum_calorie > L:
        return
    if(sub_sum_score > result):
        result = sub_sum_score
    #인덱스 유효성 검사
    if idx == N:
        return
    else:
        #현재 idx에 해당하는 재료를 선택한 경우
        subset_sum(idx+1, sub_sum_score + scoreAndCal[idx][0], sub_sum_calorie + scoreAndCal[idx][1])
        #현재 idx에 해당하는 재료를 선택하지 않는 경우
        subset_sum(idx+1, sub_sum_score, sub_sum_calorie)

testCase = int(input())
result_str = []
for tc in range(testCase):
    result = 0
    N,L = map(int,input().split())
    scoreAndCal = [([0] * 2) for i in range(N)]
    for i in range(N):
        scoreAndCal[i]= list(map(int,input().split()))
    subset_sum(0,0,0)
    result_str.append(f'#{tc+1} {result}')
print('\n'.join(result_str))
