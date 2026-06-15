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

        while True:
            nextnode = None
            idx = -1
            for i in range(k):
                if not lists[i]:
                    continue
                if not nextnode or lists[i].val < nextnode.val:
                    nextnode = lists[i]
                    idx = i
            if not nextnode:
                break
            
            curr.next = nextnode
            lists[idx] = lists[idx].next
            curr = curr.next

        return dummy.next

        

        