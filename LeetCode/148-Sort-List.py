# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        p = head
        lst: List = []  
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head

    # 인스턴스의 모든 val 을 리스트에 담아 내장함수로 정렬후 다시 ListNode 객체로 만들어 return 하는 방식
