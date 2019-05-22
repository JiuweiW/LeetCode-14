class Solution {
 public:
  Solution(ListNode* head) {
    privateHead = head;
    for (auto curr = head; curr; curr = curr->next) len++;
  }

  int getRandom() {
    int n = rand() % len;
    ListNode* curr = privateHead;
    while (n-- > 0) curr = curr->next;
    return curr->val;
  }

 private:
  ListNode* privateHead;
  int len = 0;
};