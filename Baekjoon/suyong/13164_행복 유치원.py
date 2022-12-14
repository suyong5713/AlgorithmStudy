N, K = map(int, input().split())
kids_list = list(map(int,input().split()))
kids_length_diff = []
#아이들이 키순서대로 서있음. 연속된 두 아이의 키차이를 저장. (N-1) 개
for i in range(N-1):
  kids_length_diff.append(kids_list[i+1] - kids_list[i])
#배열을 정렬하여 키차이가 가장 큰 두 아이를 경계로 조를 나눔.
#예를들어 1 3 5 6 10 의 아이들이 있다면
#키차이는 2, 2, 1, 4이고 정렬하면 1, 2, 2, 4이다.
#이때 3개의 조를 만들고자 하면 두번 가르면 된다.(oo/oo/o)
#가장 키차이가 큰 경우를 두가지 선택하여 가른다.
#두 아이를 갈라서 다른 조원으로 만들면 키 차이가 무효해진다. 따라서 diff[:N-K]까지만 더한다.
#N-K인 이유는 N명의 아이들의 키차이 개수 -> N-1개, K개의 조를 만들 때 갈라야하는 횟수 -> K - 1개.
#N-1개에서 K-1개를 빼면 N-K가 된다.
kids_length_diff.sort()
print(sum(kids_length_diff[:N-K]))
