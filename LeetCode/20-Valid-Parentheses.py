class Solution:
    def isValid(self, s: str) -> bool:
        determine = {")":"(", "}":"{", "]":"["}
        stack_list = []

        for idx, i in enumerate(s):
            if i in "([{":
                stack_list.append(i)
                continue

            if  len(stack_list) > 0 and determine[i] == stack_list[-1]:
                stack_list.pop()

            else:
                return False

        if len(stack_list) == 0:
            return True
        return False