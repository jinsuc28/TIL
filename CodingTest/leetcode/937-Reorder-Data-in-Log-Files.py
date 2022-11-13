class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        digits = []
        
        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)
        
        letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
        
        '''
        배운 점
        isalpha => 문자열이 문자인지 bool형태로 판별
        isdigit => 문자열이 숫자인지 bool형태로 판별
        
        sort 는 변수 재설정 안해도 됨
        key, lambda 이용하여서 정렬 가능(정렬 기준도 여러개 설정 가능 ex) split()[1], split()[0] 처럼)
        
        '''


        return letters + digits