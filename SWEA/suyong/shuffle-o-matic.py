def shuffle(x,left,right):
  #x가 N-1인 경우 왼쪽 절반과 오른쪽 절반 위치를 바꾸는 것과 동일
  if x == N-1:
    return right + left
  #left리스트 앞쪽에 0을 채워 오른쪽 카드뭉치가 들어갈 자리 확보
  left = ([0]*(N//2)) + left
  for i in right:
    #x가 1씩 줄어들면서 삽입되는 위치 변경
    if x > 0:
      left.insert(-x,i)
      x -= 1
    #x가 0이 되면 나머지 카드들은 제일 뒤에 삽입.
    elif x == 0:
      left.append(i)
  temp = []
  #임의로 left리스트에 채웠던 0 제거
  for i in left:
    if i != 0:
      temp.append(i)
  return temp

def dfs(depth,num_list):
  global sorted_list, re_sorted_list, min_value
  #5번 초과로 섞으면 실패
  if depth > 5:
    return
  #현재 카드들이 정렬된 상태이면 성공
  if num_list == sorted_list or num_list == re_sorted_list:
    if min_value > depth:
      min_value = depth
    return
  #정렬되지 않았다면 다시 섞기
  #x가 0일때에는 카드가 섞이지 않기 때문에 1부터 시작.
  for i in range(1,N):
    dfs(depth+1,shuffle(i,num_list[:N//2],num_list[N//2:]))
  return

testCase = int(input())
for tc in range(testCase):
  min_value = float("inf")
  N = int(input())
  number = list(map(int,input().split()))
  sorted_list = list(sorted(number))
  re_sorted_list = sorted_list[::-1]
  dfs(0, number[:])
  if min_value == float("inf"):
    print("#{} {}".format(tc+1, -1))
  else:
    print("#{} {}".format(tc+1,min_value))