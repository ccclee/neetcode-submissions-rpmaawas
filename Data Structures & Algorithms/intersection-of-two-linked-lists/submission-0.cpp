/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        unordered_set<ListNode*> nodes;
        ListNode* curr = headA;
        while(curr!= nullptr){
            nodes.insert(curr);
            curr = curr->next;
        }
        ListNode* temp = headB;
        while (temp!= nullptr){
            if (nodes.count(temp)){
                return temp;
            }
            temp = temp -> next;
        }
        return temp;
        
    }
};