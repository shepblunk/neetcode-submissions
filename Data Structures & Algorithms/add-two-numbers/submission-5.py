# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        carry = 0
        res = ListNode(0)
        head = res
        while curr is not None or curr2 is not None:
            val1 = curr.val if curr is not None else 0
            val2 = curr2.val if curr2 is not None else 0

            somme = val1 + val2 + carry
            reste = somme % 10

            head.next = ListNode(reste)

           
            carry = somme // 10

            head = head.next
            curr = curr.next if curr is not None else None
            curr2 = curr2.next if curr2 is not None else None

        if carry != 0:
            head.next = ListNode(carry)


        return res.next
        