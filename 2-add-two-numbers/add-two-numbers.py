# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummynode = ListNode(-1)
        curr = dummynode 
        
        temp1 = l1
        temp2 = l2 
        carry = 0 

        while temp1 is not None or temp2 is not None:

            sumval = carry 
            if temp1 is not None :
                sumval += temp1.val

            if temp2 is not None:
                sumval += temp2.val 

            
            new_node = ListNode(sumval % 10) 
            carry = sumval // 10 
            
            
            curr.next = new_node
            curr = curr.next 

            if temp1 is not None :
                temp1 = temp1.next 

            if temp2 is not None :
                temp2 = temp2.next 


        if carry :
            new_node = ListNode(carry)
            curr.next  = new_node 

            
        
        return dummynode.next

        