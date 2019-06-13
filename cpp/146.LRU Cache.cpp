#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

class Node{
public:
    Node *pre;
    Node *next;
    int key;
    int val;
    Node(int _key, int _val): key(_key), val(_val), pre(NULL), next(NULL){}
//    ~Node(){
//        pre = NULL;
//        next = NULL;
//    }
};


class LRUCache {
private:
    Node *headNode;
    Node *tailNode;
    int cap;
    map<int, Node*>lru_map;
    map<int, Node*>::iterator it;

    void remove2tail(Node *node) {
        node -> pre -> next =  node -> next;
        node -> next -> pre = node -> pre;
        node -> next = tailNode;
        node -> pre = tailNode -> pre;
        tailNode -> pre -> next = node;
        tailNode -> pre = node;
    }
    void removeNode(){
        Node *removeNode = headNode -> next;
        removeNode -> next -> pre = headNode;
        headNode -> next = removeNode -> next;
        lru_map.erase(removeNode->key);
        delete(removeNode);
    }


public:
    LRUCache(int capacity) {
        headNode = new Node(-1, -1);
        tailNode = new Node(-1, -1);
        headNode -> next = tailNode;
        tailNode -> pre = headNode;
        cap = capacity;
    }

    int get(int key) {
        it = lru_map.find(key);
        if (it == lru_map.end())
            return -1;
        else {
            Node *tmpNode = it -> second;
            remove2tail(tmpNode);
            return tmpNode -> val;
        }
    }

    void put(int key, int value) {
        it = lru_map.find(key);
        if (it == lru_map.end()){
            if (lru_map.size() == cap)
                removeNode();
            Node *insertNode = new Node(key, value);
            insertNode -> next = tailNode;
            insertNode -> pre = tailNode -> pre;
            tailNode -> pre -> next = insertNode;
            tailNode -> pre = insertNode;
            lru_map[key] = insertNode;
        }
        else{
            Node *tmpNode = it -> second;
            tmpNode -> val = value;
            remove2tail(tmpNode);
        }
    }
};
