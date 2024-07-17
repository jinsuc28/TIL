class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int)-> str:
            while left>=0 and right < len(s) and s[left] ==s[right]:
                left -=1
                right +=1
            return s[left + 1:right]
    
        if len(s)<2 or s==s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
       

'''

슬라이싱과 s[3]처럼 인덱스로직접 조회하는 것은 숫자를 표기하는 방식이 다르므로 주의가 필요하다.
예를 들어 s = '12345' 일 때, s[l:3]은 23이 나오지만 s[3]은 4가 나온다. 
즉, 슬라이싱은 n―1만큼 출력되며, 인덱스 조회는 해당 인덱스의 값이 나온다. 
이 부분은 실제 코딩 테스트 시에도 상당히 헷갈리는 부분이며, 
버그의 주범이 되므로 반드시 잘 숙 지해야 한다 이제 슬라이딩 
윈도우가 다음과 같이 문자열 처음부터 끝까지 우측으로 이동한다

잘 숙지하자 
이 문제는 다음에 다시한번 풀어보자

''' 
