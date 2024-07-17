class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower( )
        # 정규식으로 불필요한 문자 필터링
        # ^ : 시작 모든 영어 및 숫자에 대해서만 split 전처리
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 술라이싱
