// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};

class Solution {
private:
    void insertNode(Node* tmpNode){
        Node* insertNode = new Node();
        insertNode -> val = tmpNode -> val;
        insertNode -> next = tmpNode -> next;
        tmpNode -> next = insertNode;
    }
    void changeRandom(Node *oldNode, Node *newNode){
        if (oldNode->random != nullptr)
            newNode -> random = oldNode->random->next;
        else
            newNode -> random = nullptr;
    }
    Node *getNewList(Node *head){
        if (head == nullptr) return nullptr;
        Node *newHead = head->next;
        Node *tmpNode1 = head, *tmpNode2 = newHead;
        while(tmpNode1 != nullptr && tmpNode2 != nullptr){
            if (tmpNode2 -> next != nullptr){
                tmpNode1 -> next = tmpNode1 -> next -> next;
                tmpNode2 -> next = tmpNode2 -> next -> next;
            }else{
                tmpNode1 -> next = nullptr;
            }
            tmpNode1 = tmpNode1->next;
            tmpNode2 = tmpNode2->next;
        }
        return newHead;
    }
public:
    Node* copyRandomList(Node* head) {
        Node* tmpNode;
        tmpNode = head;
        while(tmpNode != nullptr){
            insertNode(tmpNode);
            tmpNode = tmpNode -> next->next;
        }
        tmpNode = head;
        while(tmpNode != nullptr){
            changeRandom(tmpNode, tmpNode->next);
            tmpNode = tmpNode->next->next;
        }  
        Node *newHead = getNewList(head);
        return newHead;
    }
};