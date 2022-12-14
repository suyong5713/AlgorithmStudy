from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    word_list = []

    for length in range(1, 6):
        prod = list(map(''.join, product(vowel, repeat=length)))
        for pw in prod:
            word_list.append(pw)

    word_list = sorted(word_list)

    for idx, wl in enumerate(word_list):
        if word == wl:
            return idx + 1

print(solution("AAAAE"))