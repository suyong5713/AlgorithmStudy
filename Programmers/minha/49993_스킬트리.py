def is_possible(skill_dict, cur_skill):
    new_cur_skill = []

    for s in cur_skill:
        if s in skill_dict.keys():
            new_cur_skill.append(skill_dict.get(s))

    is_ordered = True
    for num in range(len(new_cur_skill)):
        if num != new_cur_skill[num]:
            is_ordered = False

    return is_ordered


def solution(skill, skill_trees):
    answer = 0
    skill_dict = dict()

    for idx, s in enumerate(skill):
        skill_dict[s] = idx

    for cur_skill in skill_trees:
        if is_possible(skill_dict, cur_skill):
            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])