# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        listee = []
        while curr:
            listee.append(curr.val)
            curr = curr.next
        print(listee)

        i,j = 0,len(listee)-1
        while i<=j:
            if listee[i] != listee[j]:
                return False
            i+=1
            j-=1

        return True

        