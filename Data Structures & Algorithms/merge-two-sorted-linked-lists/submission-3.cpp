/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* cur1 = list1;
        ListNode* cur2 = list2;
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while(cur1 && cur2){
            if(cur1->val <= cur2->val){
                tail->next = cur1;
                cur1 = cur1->next;
            } else {
                tail -> next = cur2;
                cur2 = cur2 -> next;
        }
        tail = tail -> next;
        }
        tail->next = cur1 ? cur1 : cur2;
        return dummy.next;
    }
};
