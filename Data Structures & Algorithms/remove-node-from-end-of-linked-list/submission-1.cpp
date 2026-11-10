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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        vector<ListNode*> v;
        for(ListNode * cur = head ; cur ; cur = cur->next) v.push_back(cur);
        int taille = v.size();
        int position = taille - n;
        if(position==0) return head->next;

        v[position-1]-> next = v[position]-> next;
        return head;
        
    }
};
