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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* temp = head;
        if (head == NULL) return head;
        while (true) {
            ListNode* new_temp = temp->next; 
            temp->next = prev;
            prev = temp;
            if (new_temp == NULL) {
                head = temp;
                break;
            }
            temp = new_temp;
        }
        return head;
    }
};
