# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while one and two:
            node = None

            if one.val <= two.val:
                node = ListNode(one.val)
                one = one.next
            else:
                node = ListNode(two.val)
                two = two.next
            
            curr.next = node
            curr = curr.next
        
        if one:
            curr.next = one
        elif two:
            curr.next = two

        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        while len(lists) > 1:
            curr = []
            for i in range(0, len(lists), 2):
                one = lists[i]
                two = lists[i + 1] if i + 1 < len(lists) else None

                curr.append(self.merge(one, two))
            
            lists = curr
        
        return lists[0]