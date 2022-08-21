# def DFS(idx, sub_sum, num_count):
#     if num_count == 3:
#         result_list.append(sub_sum)
#         return
#     if idx == 7:
#         return
#     else:
#         #현재 인덱스 선택
#         DFS(idx+1, sub_sum + num_list[idx], num_count+1)
#         #현재 인덱스 선택 안함
#         DFS(idx+1, sub_sum, num_count)

testCase = int(input())
result_str = []
for tc in range(testCase):
    num_list = list(map(int,input().split()))
    result = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                result.append(num_list[i] + num_list[j] + num_list[k])
    result_str.append(f'#{tc + 1} {sorted(list(set(result)))[-5]}')
print('\n'.join(result_str))
