testCase = int(input())
for tc in range(testCase):
  N,M = map(int,input().split())
  result = "OFF"
  if M != 0:
    if format(M,"b")[::-1][:N] == "1"*N:
      result = "ON"
  print("#{} {}".format(tc+1, result))