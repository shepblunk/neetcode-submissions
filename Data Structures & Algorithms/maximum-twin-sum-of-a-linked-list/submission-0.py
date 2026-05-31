# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        liste = []
        while curr:
            liste.append(curr.val)
            curr = curr.next

        left,right = 0,len(liste)-1
        best = 0
        while left<right:
            x = liste[left] + liste[right]
            best = max(x,best)
            left += 1
            right -= 1

        return best


        