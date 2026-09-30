# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None
        prev = None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        

        