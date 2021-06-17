# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummyhead = ListNode(0)
#         carry = 0
#         curr = dummyhead
        
#         while l1 or l2:
#             if l1:
#                 l1_val = l1.val
#             else:
#                 l1_val = 0
                
#             if l2:
#                 l2_val = l2.val
#             else:
#                 l2_val = 0
                
#             sum_ = l1_val + l2_val + carry
            
#             curr.next = ListNode(sum_ % 10)
#             curr = curr.next
#             carry = sum_//10
            
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
                
#         if carry:
#             curr.next = ListNode(carry)
            
#         return dummyhead.next

# l1 = [2,4,3] 
# l2 = [5,6,4]
# s = Solution()
# s.addTwoNumbers(l1,l2)

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val, next=None):
       self.val = val
       self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode()
        curr = dummyhead
        carry = 0
        while(l1 != None or l2 != None):
            l1val = l1.val if l1 != None else 0
            l2val = l2.val if l2 != None else 0
            sum1 = carry + l1val + l2val
            carry = sum1//10
            curr.next = ListNode(sum1 % 10)
            curr = curr.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
            
        if carry > 0: curr.next = ListNode(carry)
        
        return dummyhead.next

if __name__ == "__main__":
    l1 = [2,4,3] 
    l2 = [5,6,4]
    s = Solution()
    s.addTwoNumbers(l1,l2)