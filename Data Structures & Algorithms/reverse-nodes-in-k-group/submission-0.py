# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        GroupPrev=dummy

        while True:
            a=self.kth(GroupPrev,k)
            if not a:
                break
            GroupNext=a.next

            #reverse
            prev,curr=a.next,GroupPrev.next

            while curr!=GroupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=GroupPrev.next
            GroupPrev.next=a
            GroupPrev=tmp
        return dummy.next
        
    def kth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
        