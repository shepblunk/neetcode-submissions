# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        res = ListNode(0)
        current_res = res


        curr1 = list1
        print(curr1)
        curr2 = list2

        while curr1!=None and curr2!=None:
            if curr1.val <= curr2.val:
                current_res.next = curr1
                curr1 = curr1.next

            else:
                current_res.next = curr2
                curr2 = curr2.next
            
            current_res = current_res.next

        if curr1 is not None:
            current_res.next = curr1
        if curr2 is not None:
            current_res.next = curr2


        return res.next

                


        