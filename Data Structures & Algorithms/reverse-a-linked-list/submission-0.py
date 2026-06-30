class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge cases / impossible cases
        if not head:
            return None
        elif head.next == None:
            return head
         
        # normal cases
        # setting up 
        prev = None
        current = head
        nextCurrent = head.next
        

        while current:
            nextCurrent = current.next
            current.next = prev
            prev = current
            current = nextCurrent 



        return prev