# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        dummy = ListNode()
        dummy.next = None
        curr = dummy

        while (curr!= None):
            nextnode = None
            idx = -1
            for i in range(k):
                if not nextnode and lists[i]:
                    nextnode = lists[i]
                    idx = i
                elif lists[i] and lists[i].val < nextnode.val:
                    nextnode = lists[i]
                    idx = i
            curr.next = nextnode
            if idx>-1:
                lists[idx] = lists[idx].next
            curr = curr.next

        return dummy.next

        

        