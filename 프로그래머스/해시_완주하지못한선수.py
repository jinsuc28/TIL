def solution(participant, completion):
    finish_dict = dict()
    for i in completion:
        if i not in finish_dict:
            finish_dict[i] = 1
        else:
            finish_dict[i] += 1
    
    for i in participant:
        if (i not in finish_dict) or (finish_dict[i] == 0):
            answer = i
        elif finish_dict[i] > 0:
            finish_dict[i] -= 1
            
    return answer