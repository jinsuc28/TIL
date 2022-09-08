def solution(clothes):
    clothes_dict = {}
    for name, types in clothes:
        if types in clothes_dict:
            clothes_dict[types] += 1
        else:
            clothes_dict[types] = 1
            
    cnt=1
    
    for i in clothes_dict:
        cnt *= (clothes_dict[i]+1)
               
    
    return cnt-1