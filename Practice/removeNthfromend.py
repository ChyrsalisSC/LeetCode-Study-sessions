class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # set up pointers
        temp  = ListNode(0,head)
        p1 = head
        p2 = temp
        
        for i in range(n-1):
            print(p1.val)             
            p1 = p1.next
           
        print("DONE")
        while (p1.next != None ):
          
            print(p2.val, p1.val)
           
            p2 = p2.next
            p1 = p1.next
       
        print("DELETE")
        print(p2.next.val)
        p2.next = p2.next.next
        
        return temp.next
