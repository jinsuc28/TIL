def solution(nums):
    poket = dict()
    num_max = len(nums)//2
    for i in nums:
        if i in poket:
            pass
        else:
            poket[i] = 0
    if num_max > len(poket):
        answer = len(poket)
    else:
        answer = num_max
    return answer