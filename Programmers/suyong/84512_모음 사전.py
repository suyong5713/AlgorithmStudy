def dfs(current, word):
    global flag
    if current == word:
      flag = True
    if len(current) == 5:
        return
    for char in char_list:
        if flag:
          break
        word_list.append(current + char)
        dfs(current + char, word)
    return
def solution(word):
    dfs("", word)
    answer = word_list.index(word) + 1
    return answer
flag = False
char_list = ['A', 'E', 'I', 'O', 'U']
word_list = []
print(len(word_list))
