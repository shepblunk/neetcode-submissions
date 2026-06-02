# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        head = None
        stack1 = []
        stack2 = []

        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next

        #print(stack1)
        #print(stack2)

        carry = 0
        while stack1 or stack2 or carry:
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0
            somme = digit1 + digit2 + carry
            #print(somme)

            reste = somme % 10
            carry = somme // 10
            new_node = ListNode(reste)
            new_node.next = head
            head = new_node

        return head
            
        