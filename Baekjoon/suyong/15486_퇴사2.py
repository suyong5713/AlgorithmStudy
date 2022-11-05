N = int(input())
T, P = [],[]
dp = [0] * (N+1)
for i in range(N):
    #기간 t, 수익 p
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)
M = 0 
for i in range(N):
    #M: 현재 날짜까지 가장 많이 번 수익.
    M = max(M,dp[i])
    #상담가능 기간 초과  
    if i + T[i] > N:  
        continue
    #오늘 상담을 진행했을때 수익과 dp에 저장된 상담 종료일 수익을 비교하여 더 큰 값을 저장.
    #예를들어 dp[3]이 5이고, i = 1, M = 1인 날짜에 기간 2, 수익 1짜리 상담을 진행했을 경우, 
    #상담을 진행하면 i = 3인 날짜에 수익이 2가되며 이 값이 dp[3]값보다 작기 때문에 저장되지 않음(상담을 진행하지 않음)
    dp[i+T[i]] = max(M+P[i],dp[i+T[i]])
print(dp)