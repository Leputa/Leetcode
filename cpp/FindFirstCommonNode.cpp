#include <iostream>
using namespace std;

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};

class Solution {
private:
    void swap_node(ListNode* &node1, ListNode* &node2){
        ListNode* tmpNode = node1;
        node1 = node2;
        node2 = tmpNode;
    }
    void swap(int &a, int&b){
        int tmp = a;
        a = b;
        b = tmp;
    }
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        cout << "emmme" << endl;
        if (pHead1 == nullptr || pHead2 != nullptr)
            return nullptr;
        ListNode *curNode1 = pHead1, *curNode2 = pHead2;
        int cnt1 = 0, cnt2 = 0;
        while(curNode1 != nullptr){
            curNode1 = curNode1 -> next;
            cnt1 += 1;
        }
        while(curNode2 != nullptr){
            curNode2 = curNode2 -> next;
            cnt2 += 1;
        }
        cout << cnt1 << cnt2 << endl;
        if (cnt2 > cnt1){
            swap_node(pHead1, pHead2);
            swap(cnt1, cnt2);
        }
        int diff = cnt1 - cnt2;
        for (int i=0; i<diff; i++) pHead1 = pHead1->next;
        while(pHead1 != nullptr && pHead2 != nullptr){
            if (pHead1 == pHead2)
                return pHead1;
            pHead1 = pHead1 -> next;
            pHead2 = pHead2 -> next;
        }
        return nullptr;
    }
};