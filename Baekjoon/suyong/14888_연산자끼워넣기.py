def perm(operator,opCount,subOp):
  global max_result, min_result
  #더이상 남은 연산자가 없을 때
  if opCount == 0:
    #연산자가 나오기 전 피연산자 초기화
    result = numbers[0]
    for i in range(len(subOp)):
      if subOp[i] == 0:
        result += numbers[i+1]
      elif subOp[i] == 1:
        result -= numbers[i+1]
      elif subOp[i] == 2:
        result *= numbers[i+1]
      elif subOp[i] == 3:
        result = result // numbers[i+1]
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    return
  for i in range(4):
    #i번째 연산자 선택
    if operator[i]:
      operator[i] -= 1
      subOp.append(i)
      #남은 연산자, 남은 연산자 개수, 현재 선택한 연산자
      perm(operator,opCount-1,subOp)
      #i번째 연산자 선택 해제
      #backtracking
      operator[i] += 1
      subOp.pop(-1)
  return


max_result, min_result = -(10**10),10**10
N = int(input())
subOp = []
numbers = list(map(int,input().split()))
operator = list(map(int,input().split()))
perm(operator,sum(operator),subOp)
print(max_result)
print(min_result)