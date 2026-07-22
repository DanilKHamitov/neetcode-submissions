# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        l1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        mid = slow.next
        slow.next = None
        curr = mid

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev

        while   l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
               

        
        



        