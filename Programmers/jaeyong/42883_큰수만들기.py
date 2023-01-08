# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기 (Level. 2 / Greedy)
# 풀이시간 : 30분

def solution(number, k):
    answer = ''
    collected = []
    
    for(i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
            
        if k == 0:
            collected += number[i:]
            break
        collected.append(num)
        
    if k > 0:
        collected = collected[:-k]
    answer = ''.join(collected)
    return answer

# ============================================================= #

def main(t, number, k, result):
    r = solution(number, k)
    print('#{}: {}, {}, {}'.format(t + 1, result == r, result, r))

if __name__ == '__main__':
    number = ['1924', '1231234', '4177252841']
    k = [2, 3, 4]
    result = ['94', '3234', '775841']

    for t in range(3):
        main(t, number[t], k[t], result[t])
