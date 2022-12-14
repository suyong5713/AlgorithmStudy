# from itertools import product
#
# def solution(word):
#     words = []
#     for i in range(1, 6):
#         words.extend(list(map(''.join, product(['A', 'E', 'I', 'O', 'U'], repeat=i))))
#     words.sort()
#     return words.index(word) + 1


# def solution(word):
#     words = []
#     alpha = 'AEIOU'
#
#     def combi(cnt, w):
#         if cnt == 5:
#             return
#         for i in range(len(alpha)):
#             words.append(w + alpha[i])
#             combi(cnt + 1, w + alpha[i])
#
#     combi(0, '')
#
#     return words.index(word) + 1


def solution(word):
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word)
    order = 781
    for i in word:
        answer += order * alpha[i]
        order = (order - 1) // 5
    return answer