class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
            
        '''
        계속 output
        [["a","e","t"],["a","n","t"],["a","b","t"]]
        나옴 type hint 때문에 이렇게 나오게 되는 것 같음
        '''
        
        '''
        https://otugi.tistory.com/268

        1.먼저 그냥 s.sort()를 쓰면 안된다. - str type에 sort()라는 메소드가 없기 때문
        (이유는 string의 경우 첫글자의 주소값으로 참조를 하기에 원본이 변경되면 안된다.)

        2.대신 sorted(s)처럼 쓰는 것은 가능하다. - 대신 return type은 list이다.

        3.이를 하나로 이어진 문자열로 만들기 위해선 ''.join을 사용하면 된다.
        '''
        
        
        '''
        리스트.sort() 는 제자리 정렬을 진행하여 결과값으로 none 뱉게된다.
        ex) ab = 리스트.sort() 하면 ab 는 none 출력함 따라서 그냥 리스트를 변수로 쓰면 된다.(정렬되어있음)
        '''
        return list(anagrams.values())