word1 = list(input())
word2 = list(input())
word1.insert(0, 0)
word2.insert(0, 0)
dp = [[0] * (len(word2)) for _ in range((len(word1)))]

for i in range(1, len(word1)):
    for j in range(1, len(word2)):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
