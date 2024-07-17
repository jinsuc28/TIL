class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0,len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -= 1


'''
슬라이싱으로 풀려고 하다 도저히 안풀려서 정답을 보니 좀 많이 허탈..
플랫폼마다 환경을 잘 알아두는 것이 중요하다는 것을 파악함
또한, 투 포인터라는 방법을 처음으로 익힐 수 있었음
'''