class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        best_word = ''
        best_word_cnt = 0
        word_dict = {}
        
        paragraph = re.sub('[^a-zA-Z-]',' ', paragraph)
        paragraph = paragraph.lower().split()
        for word in paragraph:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
                
        for key,value in word_dict.items():     
            if (value > best_word_cnt) & (key not in banned):
                best_word = key
                best_word_cnt = value
                
        return best_word
    '''
    
    If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
    
    split(None) None 이면 다르게 동작하는데 모든 공백(개수 상관 없이) 기준으로 나뉘게 됨
    '''

    
    '''
    더 쉽게
    
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().spalit() if word not in banned]
    
    counts = collections.defaultdict(int) 
    # 딕셔너리 넣으면 자동으로 int value 생성, 있는지 확인할 필요가 없어짐
    for word in words:
        counts[word] += 1
        
    # max, min 모두 key 사용 가능 dict(key, value) max(key) max의 key는 dict의 key를 말하며 이를 dict.get 으로 value를
    뽑아 최대값을 찾은 다음에 여기서 key를 내보내게 된다.
    return max(counts, key=counts.get)
    
    혹은
    
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
    
    '''