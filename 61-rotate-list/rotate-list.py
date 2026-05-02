class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        tail = head 
        n = 1
        while tail.next:
            tail = tail.next
            n+=1
        k%=n
        if k==0:
            return head
        tail.next = head

        for _ in range(n-k):
            tail = tail.next

        new_head = tail.next
        tail.next = None
        return new_head