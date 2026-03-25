class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Find middle
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split into 2 halves
        mid = slow.next
        slow.next = None
        
        # Step 3: Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 4: Merge sorted halves
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next