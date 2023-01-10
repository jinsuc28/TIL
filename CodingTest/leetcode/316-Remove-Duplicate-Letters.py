class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]

            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

'''
어렵네 다시 풀어보자
'''




if __name__ == "__main__":
    sol = Solution()
    sol.removeDuplicateLetters("cdadabcc")