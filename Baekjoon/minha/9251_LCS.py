str1 = ' ' + input()
str2 = ' ' + input()

graph = [[0] * (len(str2)) for _ in range(len(str1))]

for i in range(1, len(graph)):
    for j in range(1, len(graph[i])):
        if str1[i] == str2[j]:
            graph[i][j] = graph[i - 1][j - 1] + 1
        else:
            graph[i][j] = max(graph[i - 1][j], graph[i][j - 1])

print(graph[-1][-1])